from Symbol import Symbol


class SymbolTable(object):
    """
    SymbolTable: Provides a symbol table abstraction. The symbol table associates the identifier names found in the
    program with identifier properties needed for compilation: type, kind, and running index.
    The symbol table for Jack programs has two nested scopes (class/subroutine).
    """
    def __init__(self):
        self._class_table = dict()
        self._subroutine_table = None
        self._counter = {'field': 0, 'local': 0, 'argument': 0, 'static': 0}

    def start_subroutine(self) -> None:
        """
        Starts a new subroutine scope (i.e. reset the subroutine symbol table)
        """
        if self._subroutine_table:
            self._subroutine_table.clear()
        else:
            self._subroutine_table = dict()
        self._counter.update({'argument': 0, 'local': 0})

    def add_symbol(self, symbol: Symbol) -> None:
        """
        Add symbol to correspond table.
        Args: symbol (Symbol) - a Symbol object to be added
        """
        symbol.id = self._counter[symbol.kind]
        self._counter[symbol.kind] += 1

        if symbol.kind in ['argument', 'local']:
            self._subroutine_table[symbol.name] = symbol
        else:
            self._class_table[symbol.name] = symbol

    def get_symbol(self, name: str) -> Symbol:
        """
        Args: name (str) - the name of the symbol to be fetched
        Returns: (Symbol) the correspond symbol object
        """
        if (symbol := self._subroutine_table.get(name, None)) is not None:
            return symbol
        elif (symbol := self._class_table.get(name, None)) is not None:
            return symbol

    def var_count(self, kind: str) -> int:
        """
        Args: kind (str) - kind value from [STATIC, FIELD, ARG, VAR]
        Returns: (int) the number of variables of the given kind already defined in the current scope.
        """
        return self._counter.get(kind, -1)

    def kind_of(self, name: str) -> str:
        """
        Args: name (str) - name of a symbol
        Returns: (str) The kind of the name identifier (STATIC, FIELD, ARG, VAR) in the current scope.
                 If the identifier is unknown in the current scope, returns 'NONE'
        """
        if (symbol := self._subroutine_table.get(name, None)) is not None:
            return symbol.kind
        elif (symbol := self._class_table.get(name, None)) is not None:
            return symbol.kind

    def type_of(self, name: str):
        """
        Args: name (str) - name of a symbol
        Returns: (str) The type of the named identifier in the current scope.
        """
        if (symbol := self._subroutine_table.get(name, None)) is not None:
            return symbol.type
        elif (symbol := self._class_table.get(name, None)) is not None:
            return symbol.type
        return None

    def index_of(self, name: str):
        """
        Args: name (str) - name of a symbol
        Returns: (int) The index assigned to the named identifier.
        """
        if (symbol := self._subroutine_table.get(name, None)) is not None:
            return symbol.id
        elif (symbol := self._class_table.get(name, None)) is not None:
            return symbol.id
        return None

    def close(self) -> None:
        """
        Clear and resets tables and counter
        """
        self._counter.clear()
        self._class_table.clear()
        self._subroutine_table = None
