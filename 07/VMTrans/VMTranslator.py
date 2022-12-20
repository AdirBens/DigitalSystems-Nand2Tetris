import argparse

from CodeWriter import CodeWriter
from Parser import Parser


class VMTranslator(object):
    """
    VM translator translate Jack VM files, yielding corresponding programs written in the Hack assembly language.
    The translator creates an output file named fileName.asm, which is stored in the same directory of the input file.
    The name of the input file may contain a file path.
    """

    def __init__(self, input_file: str):
        self.vm_file = input_file
        self.asm_out_file = input_file.replace(".vm", ".asm")
        self.parser = Parser(input_file)
        self.code_writer = CodeWriter(self.parser, self.asm_out_file)
        # add directory case

    def translate(self) -> None: #ADD VERBOSE?
        """
        :param verbose:
        :return: None
        """
        while self.parser.has_more_commands():
            self.parser.advance()
            asm_out_file.


def main():
    cli_parser = argparse.ArgumentParser(prog="VMTranslator", description="translates from jack code to assembly code")
    cli_parser.add_argument('file_name', action='store', required=True,
                            help="path to fileName.vm - path to a text file containing VM commands")
    args = cli_parser.parse_args()

    vm_translator = VMTranslator(args.file_name)
    vm_translator.translate()


if __name__ == "__main__":
    main()
