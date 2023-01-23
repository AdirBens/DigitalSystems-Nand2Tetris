class Symbol(object):
    """
    JackSymbol Object
    """
    def __init__(self, symbol_kind: str = None, symbol_type: str = None, name: str = None):
        self.name = name
        self.type = symbol_type
        self.kind = symbol_kind
        self.id = None
        self.reused = False

    def set_name(self, name: str) -> None:
        self.name = name

    def set_type(self, symbol_type: str) -> None:
        self.type = symbol_type

    def set_kind(self, symbol_kind: str) -> None:
        self.kind = symbol_kind

    def set_id(self, symbol_id: int) -> None:
        self.id = symbol_id

    def __str__(self) -> str:
        return f"[Symbol] name: {self.name}, type: {self.type}, kind: {self.kind}, id: {self.id} "
