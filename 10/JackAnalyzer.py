import argparse
import pathlib

from error import InvalidInputFileError
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer


class JackAnalyzer(object):
    """
    Top-level driver that sets up and invokes the other modules;
    """
    _input_files = None
    _output_file = None

    def __init__(self, input_path: str):
        self._set_io_files(input_path)
        self.tokenizer = JackTokenizer()
        self.engine = CompilationEngine(output=self._output_file, tokenizer=self.tokenizer)

    def close(self) -> None:
        """
        JackAnalyzer destructor - close this tokenizer and engine
        """
        self.tokenizer.close()
        self.engine.close()

    def analyze_code(self) -> None:
        """
        """
        for prog in self._input_files:
            self.tokenizer.set_input_file(prog)
            if self.tokenizer.has_more_tokens():
                self.engine.compile_class()
        self.close()

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
            self._input_files = [path]
            self._output_file = path.with_suffix(".xml")

        elif path.is_dir() and path.glob("*.jack").__sizeof__():
            self._input_files = list(path.glob("*.jack"))
            self._output_file = path.joinpath(f"{path.absolute().parts[-1]}.xml")
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
