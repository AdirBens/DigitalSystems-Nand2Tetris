import pathlib


class JackTokenizer(object):
    """
    Removes all comments and white space from the input stream and breaks it into Jack-language tokens,
    as specified by the Jack grammar.
    """

    INPUT_FILE = None

    def __init__(self):
        """
        Opens the input file/stream and gets ready to tokenize it.
        Args:
        """
        pass

    def set_input_file(self, input_file: pathlib.Path) -> None:
        """
        Sets JackTokenizer's input_file to given file
        Args:
            input_file (pathlib.Path) -
        Returns: None
        """
        self.INPUT_FILE = input_file

    def has_more_tokens(self) -> bool:
        """
        Returns: true if there are more commands in the input, else false.
        """
        pass

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
    