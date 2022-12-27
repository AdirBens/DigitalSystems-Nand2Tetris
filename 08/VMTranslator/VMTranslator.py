import argparse
import time
from glob import glob
from CodeWriter import CodeWriter
from Parser import Parser


class VMTranslator(object):
    """
    VM translator translate Jack VM files, yielding corresponding programs written in the Hack assembly language.
    The translator creates an output file named fileName.asm, which is stored in the same directory of the input file.
    The name of the input file may contain a file path.
    """
    def __init__(self, vm_files: str):
        self.vm_files = self._load_program_path(vm_files)
        self.parser = None
        self.code_writer = None

    def translate(self) -> None:
        """
        Orchestrate Translation VM Commands to HackAssembly process.
        Returns: None.
        """
        for vm_file in self.vm_files:
            self._set_file_to_modules(vm_file)
            while self.parser.has_more_commands():
                self.parser.advance()
                current_command = self.parser.get_current_command()
                if current_command.command_type == 'C_ARITHMETIC':
                    self.code_writer.write_arithmetic(current_command)
                elif current_command.command_type != 'C_RETURN':
                    self.code_writer.write_push_pop(current_command)
                else:
                    continue
                    #TODO: append branches according to new `writer` methods in CodeWriter

        log_info = self._get_running_info()
        self.parser.close()
        self.code_writer.close()
        self._log_file(log_info, header=True, stdout=True)

    def _log_file(self, log_info: str, header: bool = False, stdout: bool = True) -> None:
        """
        Generate Log form translation session info.
        Args:
            log_info (str): translation session info,
                            includes number of parsed lines, and number of asm code lines produced
            header (bool): if true append info header to the head of produced .asm file
            stdout (bool): if true print translation session info to stdout.
        Returns: None.
        """
        if stdout:
            print(log_info)
        if header:
            with open(self.vm_files.replace('.vm', '.asm'), 'r') as f:
                content = f.readlines()
            with open(self.vm_files.replace('.vm', '.asm'), 'w') as f:
                f.write(log_info.replace("\n", "\n// ") + 2 * "\n")
                f.writelines(content)

    def _get_running_info(self) -> str:
        """
        Collect info about translation session from parser and code writer:
            - get the number of parsed line by Parser
            - get the number of asm code lines produced by CodeWriter
        Returns: running_info (str)
        """
        parsed = self.parser.get_lines_parsed()
        produced = self.code_writer.get_lines_produced()
        indent1, indent2, sep = 1 * ' ' + '[+]', 5 * ' ' + '[>]', 24 * '-'
        t = time.ctime()
        file = self.vm_files.split('/')[-1]

        return "\n".join(['', f'{sep}{t}{sep}', f'VMTranslator - Translation Of {file} to HackAssembly code.',
                          f'{indent1} Translation end successfully.',
                          f'\n'.join([f'{indent2} {parsed} VM Code lines parsed',
                                      f'{indent2} {produced} ASM Code lines produced.',
                                      f'{indent2} Translation ratio is {produced / parsed}']), f'{sep}{sep}{sep}'])

    def _set_file_to_modules(self, vm_file) -> None:
        if self.code_writer is None and self.parser is None:
            self.parser = Parser(vm_file)
            self.code_writer = CodeWriter(vm_file)
        else:
            self.parser.close()
            self.parser = Parser(vm_file)
            self.code_writer.set_file_name(vm_file)
    @staticmethod
    def _load_program_path(program_path: str) -> list:
        if program_path.endswith('.vm'):
            vm_files = [program_path]
        else:
            vm_files = glob(r'{}/*.vm'.format(program_path))
            if not any([file.endswith('Main.vm') for file in vm_files]):
                raise FileNotFoundError('[-] VMTranslator: Main.vm is missing.')
            elif not any([file.endswith('Sys.vm') for file in vm_files]):
                raise FileNotFoundError('[-] VMTranslator: Sys.vm is missing.')
            else:
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
