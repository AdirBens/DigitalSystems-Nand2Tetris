import pathlib

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
        Args:
        """
        self._file_iterator = None
        self.current_token = None

    def set_input_file(self, input_path: pathlib.Path) -> None:
        """
        Open input file and Sets it as JackTokenizer's input_file
        Args:
            input_path (pathlib.Path) -
        Returns: None
        """
        if self._file_iterator:
            self.close()
        self._file_iterator = open(input_path, 'r')
        self._file_iterator.seek(0)

    def has_more_tokens(self) -> bool:
        """
        Returns: true if there are more commands in the input, else false.
        """
        cursor = self._file_iterator.tell()
        has_more_tokens = bool(self._file_iterator.read(1))
        self._file_iterator.seek(cursor)

        return has_more_tokens

    def advance(self) -> None:
        """
        Gets the next token from the input and makes it the current token.
        This method should only be called if @has_more_tokens() is true.
        Returns: None
        """
        self.set_cursor_to_code()
        cursor = self._file_iterator.tell()
        buffer = self._file_iterator.readline()
        with_whites = len(buffer)
        buffer = buffer.lstrip()
        whites = with_whites - len(buffer)

        token = None
        terminal = None
        if token := Syntax.TERMINALS.get("inline_comment").match(buffer):
            terminal = "inlineComment"

        elif token := Syntax.TERMINALS.get("symbol").match(buffer):
            terminal = "symbol"
            token = token.group(0)
            if token == '<':
                token = '&lt;'
                whites -= 2
            if token == '>':
                token = '&gt'
                whites -= 2

        elif token := Syntax.TERMINALS.get("keyword").match(buffer):
            terminal = "keyword"
            token = token.group(0)

        elif token := Syntax.TERMINALS.get("integer_constant").match(buffer):
            terminal = "integerConstant"
            token = token.group(0)

        elif token := Syntax.TERMINALS.get("string_constant").match(buffer):
            terminal = "stringConstant"
            token = token.group(1)
            whites += 2

        elif token := Syntax.TERMINALS.get("identifier").match(buffer):
            terminal = "identifier"
            token = token.group(0)

        if token:
            self.current_token = Token(token_type=terminal, token_value=token)
            # print("ter: " + terminal + " tok: " + token.__str__())
            self._file_iterator.seek(cursor + whites + len(token))

        else:
            self.current_token = None


            # for terminal, matcher in Syntax.TERMINALS.items():
            #     if token := matcher.match(buffer):
            #         if terminal == "inline_comment":
            #             break
            #         elif terminal == "keyword":
            #             print(token.__repr__())
            #             token = token.group(0)
            #             break
            #         else:
            #             print(token.__repr__())
            #             print(token.groups())
            #             token = token.group(0)
            #             break

    def token_type(self):
        """
        Returns: The type of the current token. one of KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST
        """
        pass

    def key_word(self):
        """
        Returns: The keyword which is the current token. Should be called only when tokenType() is KEYWORD.
                    one of CLASS, METHOD, FUNCTION, CONSTRUCTOR, INT, BOOLEAN, CHAR, VOID, VAR, STATIC, FIELD, LET,
                    DO, IF, ELSE, WHILE, RETURN, TRUE, FALSE, NULL, THIS
        """
        pass

    def symbol(self) -> chr:
        """
        Returns: (chr) The character which is the current token. Should be called only when tokenType() is SYMBOL.
        """
        pass

    def identifier(self) -> str:
        """
        Returns: (str) The identifier which is the current token. Should be called only when tokenType() is IDENTIFIER.
        """
        pass

    def int_val(self) -> int:
        """
        Returns: (int) The integer value of the current token. Should be called only when tokenType() is INT_CONST.
        """
        pass

    def string_val(self) -> str:
        """
        Returns: (str) The string value of the current token, without the double quotes.
                       Should be called only when tokenType() is STRING_CONST.
        """
        pass

    def set_cursor_to_code(self) -> None:
        """

        """
        cursor = self._file_iterator.tell()
        buffer = self._file_iterator.readline()

        while buffer.lstrip().startswith("//") or buffer == "\n":
            cursor = self._file_iterator.tell()
            buffer = self._file_iterator.readline()

        if buffer.lstrip().startswith("/*"):
            end_multiline = False
            while not end_multiline:
                end_multiline = buffer.endswith("*/\n")
                cursor = self._file_iterator.tell()
                buffer = self._file_iterator.readline()

        self._file_iterator.seek(cursor)

    def close(self) -> None:
        """
        Closes The Input File
        Returns: None
        """
        self._file_iterator.close()
