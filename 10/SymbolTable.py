# DO NOT TOUCH - PROJECT 11

class SymbolTable(object):
    """
    SymbolTable: Provides a symbol table abstraction. The symbol table associates the identifier names found in the
    program with identifier properties needed for compilation: type, kind, and running index.
    The symbol table for Jack programs has two nested scopes (class/subroutine).
    """

    def __init__(self):
        pass

    def start_subroutine(self) -> None:
        """
        Starts a new subroutine scope (i.e. reset the subroutine symbol table)
        Args: None
        Returns: None
        """
        pass

    def define(self, name: str, itype: str, kind: str) -> None:
        """
        Defines a new identifier of a given name, type, and kind and assigns it a running index.
        STATIC and FIELD identifiers have a class scope, while ARG and VAR identifiers have a subroutine scope.
        Args:
            name (str) -
            itype (str) -
            kind (str) - kind value from [STATIC, FIELD, ARG, VAR]
        Returns: None
        """
        pass

    def var_count(self, kind: str) -> int:
        """
        Returns the number of variables of the given kind already defined in the current scope.
        Args:
            kind (str) - kind value from [STATIC, FIELD, ARG, VAR]
        Returns:
            (int)
        """
        pass

    def kind_of(self, name: str):  # -> Kind:
        """
        Args:
             name (str) -
        Returns: The kind of the name identifier (STATIC, FIELD, ARG, VAR) in the current scope.
                 If the identifier is unknown in the current scope, returns 'NONE'
        """
        pass

    def type_of(self, name: str) -> str:
        """
        Args:
             name (str) -
        Returns: The type of the named identifier in the current scope.
        """
        pass

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str) -
        Returns: The index assigned to the named identifier.
        """
        pass
