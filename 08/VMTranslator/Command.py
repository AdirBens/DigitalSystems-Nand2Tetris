class Command(object):
    """
    Command object initialize with VMCommand string.
    The Command object is taking care of extracting command's components from VMCommand string,
    and provide convenient and safe access to command's components.
    """
    def __init__(self, command: str):
        self._vm_string = command
        self._cmd_types = self._load_types()
        self._command_type = self._extract_type()
        self._operation = self._extract_operation()
        self._arg1 = self._extract_arg1()
        self._arg2 = self._extract_arg2()

    def __str__(self):
        return self._vm_string

    def __repr__(self):
        return 'Command {}: operation={}({}) arg1={} arg2={}'.format(self._vm_string, self._operation,
                                                                     self._command_type,
                                                                     self._arg1, self._arg2)

    def _extract_type(self) -> str:
        """
        Returns: (str) command type keyword
        """
        return "".join([self._cmd_types[k] for k in self._cmd_types.keys() if k in self._vm_string])

    def _extract_operation(self) -> str:
        """
        Returns: (str) command operation keyword
        """
        return "".join([k for k in self._cmd_types.keys() if k in self._vm_string])

    def _extract_arg1(self) -> str:
        """
        Returns: (str) arg1 from VMCommand string, and modify it according to command type and operation.
                       if Command type is C_RETURN returns None.
        """
        arg1 = None
        if self._command_type == 'C_ARITHMETIC':
            arg1 = self._extract_operation()
        elif self._command_type != 'C_RETURN':
            arg1 = self._vm_string.split()[1]
        return arg1

    def _extract_arg2(self) -> str:
        """
        Returns: (str) arg2 from VMCommand string, and modify it according to command type and operation.
                       if command type not in C_PUSH, C_POP, C_FUNCTION, C_CALL returns None.
        """
        arg2 = None
        if self._command_type in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            arg2 = self._vm_string.split()[2]
            if self._arg1 == 'pointer':
                arg2 = 'THAT' if int(arg2) else 'THIS'
        return arg2

    @property
    def command_type(self) -> str:
        return self._command_type

    @property
    def operation(self) -> str:
        return self._operation

    @property
    def arg1(self) -> str:
        return self._arg1

    @property
    def arg2(self) -> str:
        return self._arg2

    @staticmethod
    def _load_types() -> dict:
        """
        Returns: (dict) dictionary holds the command types according to command operation string
        """
        arithmetic = {k: 'C_ARITHMETIC' for k in ['add', 'sub', 'and', 'or', 'neg', 'not', 'eq', 'gt', 'lt']}
        commands = {k: 'C_{}'.format(k.split('-')[0].upper())
                    for k in ['push', 'pop', 'label', 'goto', 'if-goto', 'function', 'return', 'call']}
        commands.update(arithmetic)
        return commands
