import argparse
import pathlib

from error import InvalidInputFileError
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer


class JackAnalyzer(object):
    """
    Top-level driver that sets up and invokes the other modules;
    """
    INPUT_FILES = None
    OUTPUT_FILE = None

    def __init__(self, input_path: str):
        self._set_io_files(input_path)
        self.TOKENIZER = JackTokenizer()
        self.ENGINE = CompilationEngine(self.OUTPUT_FILE, debug=True)

    def analyze_code(self) -> int:
        """
        Returns: (int) analysis status code
        """
        for prog in self.INPUT_FILES:
            self.TOKENIZER.set_input_file(prog)
            while self.TOKENIZER.has_more_tokens():
                self.TOKENIZER.advance()
                token = self.TOKENIZER.current_token
                if token:
                    self.ENGINE.append_node(token)
        # TODO: Consider to change the return value to status code
        return 0

    def _set_io_files(self, path: str) -> None:
        """
        Validate that given input-path is either a single .jack file, Or directory contains one or more .jack files,
        and assign theme to the INPUT_FILES
        Args:
            path (str) - input program path
        Returns: None
        Raises: InvalidInputFileError if the path is not valid
        """
        path = pathlib.Path(path)
        if path.is_file() and path.suffix == ".jack":
            self.INPUT_FILES = [path]
            self.OUTPUT_FILE = path.with_suffix(".xml")

        elif path.is_dir() and path.glob("*.jack").__sizeof__():
            self.INPUT_FILES = list(path.glob("*.jack"))
            self.OUTPUT_FILE = path.joinpath(f"{path.absolute().parts[-1]}.xml")
        else:
            raise InvalidInputFileError("The given path is not a single .jack file "
                                        "nor directory contains one or more .jack file")


def main():
    cli_parser = argparse.ArgumentParser(prog="JackAnalyzer",
                                         description="SyntaxAnalyzer - As Jack Compilation First Stage")
    cli_parser.add_argument('program_path', action='store', help="path to .jack file or directory contains .jack files")
    args = cli_parser.parse_args()

    analyzer = JackAnalyzer(args.program_path)
    analyzer.analyze_code()


if __name__ == "__main__":
    main()
