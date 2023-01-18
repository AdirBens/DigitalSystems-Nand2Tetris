

class Symbol(object):
    """
    JackSymbol Object
    """
    def __init__(self, name: str = None, symbol_type: str = None, symbol_kind: str = None):
        self.name = name
        self.type = symbol_type
        self.kind = symbol_kind
        self.id = None
        self.reused = False

    def set_name(self, name: str):
        self.name = name

    def set_type(self, symbol_type: str):
        self.type = symbol_type

    def set_kind(self, symbol_kind: str):
        self.kind = symbol_kind

    def set_id(self, symbol_id: int):
        self.id = symbol_id

    def __str__(self):
        return f"[Symbol] name: {self.name}, type: {self.type}, kind: {self.kind}, id: {self.id} "

    def __repr__(self):
        """
        Returns: This token's represents as a XML node
        """
        return f"<TRAVOR {self.type}> {self.name} , {self.type} , {self.kind} , {self.id} </{self.type}>"
