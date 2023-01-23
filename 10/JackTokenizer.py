from Syntax import Syntax
from Token import Token


class JackTokenizer(object):
    """
    Removes all comments and white space from the input stream and breaks it into Jack-language tokens,
    as specified by the Jack grammar.
    """
    def __init__(self):
        """
        Opens the input file/stream and gets ready to tokenize it.
        """
        self.file_iterator = None
        self._current_token = None

    @property
    def current_token(self):
        return self._current_token

    def set_input_file(self, input_path) -> None:
        """
        Open input file and Sets it as JackTokenizer's input_file
        Args: input_path (.jack program path as string or as a pathlib.Path object)
        """
        if self.file_iterator:
            self.close()
        self.file_iterator = open(input_path, 'r')
        self.file_iterator.seek(0)

    def has_more_tokens(self) -> bool:
        """
        Returns: true if there are more commands in the input, else false.
        """
        cursor = self.file_iterator.tell()
        has_more_tokens = bool(self.file_iterator.read(1))
        self.file_iterator.seek(cursor)

        return has_more_tokens

    def advance(self) -> None:
        """
        Gets the next token from the input and makes it the current token.
        This method should only be called if @has_more_tokens() is true.
        """
        self._current_token = None
        self.set_cursor_to_code()
        cursor = self.file_iterator.tell()
        buffer = self.file_iterator.readline()

        whites, buffer = self.left_strip(buffer)

        for terminal, matcher in Syntax.TERMINALS.items():
            if token := matcher.match(buffer):
                token_value = token.group(0)
                if terminal != "inlineComment":
                    self._current_token = Token(token_type=terminal, token_value=token_value)
                self.file_iterator.seek(cursor + whites + len(token_value))
                break

    def set_cursor_to_code(self) -> None:
        """
        Sets the file cursor to the next actual code,
        by ignoring one-line and multi-lines comments, and blank lines
        """
        cursor = self.file_iterator.tell()
        buffer = self.file_iterator.readline()

        while buffer.lstrip().startswith("//") or buffer.isspace():
            cursor = self.file_iterator.tell()
            buffer = self.file_iterator.readline()

            if buffer.lstrip().startswith("/*"):
                end_multiline = False
                while not end_multiline:
                    end_multiline = buffer.endswith("*/\n")
                    cursor = self.file_iterator.tell()
                    buffer = self.file_iterator.readline()

        self.file_iterator.seek(cursor)

    @staticmethod
    def left_strip(string: str) -> (int, str):
        """
        Args: string (str)
        Returns: (int) The number of whitespaces removed from left
                 (str) The string after string.lstrip()
        """
        before = len(string)
        string = string.lstrip()
        return before - len(string), string

    def close(self) -> None:
        """
        Closes The Input File
        """
        self.file_iterator.close()
