class Token(object):
    """

    """

    def __init__(self, token_type: str, token_value: str):
        self.token_type = token_type
        self.token_value = token_value

    def __str__(self):
        return f"<{self.token_type}> {self.token_value} </{self.token_type}>"
