class Token(object):
    """
    Represents a single `Token`.
    Provides encapsulation and safe access to token's data
    """
    def __init__(self, token_type: str, token_value: str):
        self._token_type = token_type
        self._token_value = token_value

    @property
    def token_type(self) -> str:
        """
        Returns: This token's type - symbol, keyword, stringConstant, integerConstant, identifier
        """
        return self._token_type

    @property
    def token_value(self) -> str:
        """
        Returns: This token's data representation.
        """
        if self.token_type == "stringConstant":
            return self._token_value[1:-1]
        else:
            return {">": "&gt;", "<": "&lt;",
                    "&": "&amp;", "\"": "&quot;"}.get(self._token_value,
                                                      self._token_value)

    def __str__(self) -> str:
        """
        Returns: This token's represents as an XML node
        """
        return f"<{self.token_type}> {self.token_value} </{self.token_type}>"

    def __eq__(self, other) -> bool:
        return self.token_value == other
