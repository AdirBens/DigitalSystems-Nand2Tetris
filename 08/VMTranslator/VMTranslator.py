import argparse
import os
from glob import glob

from Logger import Logger
from CodeWriter import CodeWriter
from Parser import Parser


class VMTranslator(object):
    """
    VM translator translate Jack VM files, yielding corresponding programs written in the Hack assembly language.
    The translator creates an output file named fileName.asm, which is stored in the same directory of the input file.
    The name of the input file may contain a file path.
    """
    def __init__(self, program_path: str):
        self._as_dir = os.path.isdir(program_path)
        self._out_file = os.path.join(program_path, os.path.basename(program_path) + '.asm') if self._as_dir \
            else program_path.replace('.vm', '.asm')

        self.vm_files = self._get_vmfiles(program_path)
        self.logger = Logger(out_file=self._out_file, prog_path=program_path)
        self.code_writer = CodeWriter(self._out_file)
        self.parser = None

    def translate(self) -> None:
        """
        Orchestrate Translation VM Commands to HackAssembly process.
        Returns: None.
        """
        if self._as_dir: self.code_writer.write_init()
        for vm_file in self.vm_files:
            self._set_file_to_modules(vm_file)
            while self.parser.has_more_commands():
                self.parser.advance()
                current_command = self.parser.get_current_command()
                if current_command.command_type == 'C_ARITHMETIC':
                    self.code_writer.write_arithmetic(current_command)
                elif current_command.command_type in ['C_PUSH', 'C_POP']:
                    self.code_writer.write_push_pop(current_command)
                elif current_command.command_type == 'C_LABEL':
                    self.code_writer.write_label(current_command)
                elif current_command.command_type == 'C_GOTO':
                    self.code_writer.write_goto(current_command)
                elif current_command.command_type == 'C_IF':
                    self.code_writer.write_if(current_command)
                elif current_command.command_type == 'C_CALL':
                    self.code_writer.write_call(current_command)
                elif current_command.command_type == 'C_FUNCTION':
                    self.code_writer.write_function(current_command)
                elif current_command.command_type == "C_RETURN":
                    self.code_writer.write_return(current_command)

        parsed, produced = self.parser.get_lines_parsed(), self.code_writer.get_lines_produced()
        self.parser.close()
        self.code_writer.close()
        self.logger.log_session(vm_parsed=parsed, asm_produced=produced, vm_files=self.vm_files, is_dir=self._as_dir,
                                header=True, stdout=True)

    def _set_file_to_modules(self, vm_file) -> None:
        if self.parser is None:
            self.parser = Parser(vm_file)
        else:
            self.parser.close()
            self.parser = Parser(vm_file)
            self.code_writer.set_file_name(vm_file)

    @staticmethod
    def _get_vmfiles(program_path: str) -> list:
        if program_path.endswith('.vm'):
            vm_files = [program_path]
        else:
            vm_files = glob(r'{}/*.vm'.format(program_path))
            if not any([file.endswith('Sys.vm') for file in vm_files]):
                raise FileNotFoundError('[-] VMTranslator: Sys.vm is missing.')
            vm_files.sort(key=lambda file: -2 if file.endswith('Sys.vm') else 1)
        return vm_files


def main():
    cli_parser = argparse.ArgumentParser(prog="VMTranslator", description="Translates from jack code to assembly code")
    cli_parser.add_argument('program_path', action='store',
                            help="path to a .vm file or directory containing .vm files")
    args = cli_parser.parse_args()

    vm_translator = VMTranslator(args.program_path)
    vm_translator.translate()


if __name__ == "__main__":
    main()
