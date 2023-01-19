# DO NOT TOUCH - PROJECT 11

class VMWriter(object):
    """
    Emits VM commands into a file, using the VM command syntax.
    """

    def __init__(self, out: str = None):
        """
        Creates a new VMWriter, set out file and prepares it for writing.
        """
        self.out_file = out

    def set_outfile(self, out_file) -> None:
        self.out_file = out_file

    def write_push(self, segment: str, index: int) -> None:
        """
        Writes a VM push command
        Args:
            segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
            index (int) -
        Returns: None
        """
        segment = {'field': 'this', 'arg': 'argument', 'var': 'local'}.get(segment, segment)
        self.out_file.write(f'push {segment} {index}\n')

    def write_pop(self, segment: str, index: int) -> None:
        """
        Writes a VM pop command
        Args:
            segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
            index (int) -
        Returns: None
        """
        segment = {'field': 'this', 'arg': 'argument', 'var': 'local'}.get(segment, segment)
        self.out_file.write(f'pop {segment} {index}\n')

    def write_arithmetic(self, command: str, op_type: str = "binary") -> None:
        """
        Writes a VM arithmetic command
        Args:
            command (str) - ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
        Returns: None
        """
        ops = {"binary": {'+': 'add', '-': 'sub', '*': 'call Math.multiply 2', '/': 'call Math.divide 2',
                          '&amp;': 'and', '|': 'or', '&lt;': 'lt', '&gt;': 'gt', '=': 'eq'},
               "unary": {'~': 'not', '-': 'neg'}}
        self.out_file.write(f'{ops.get(op_type).get(command)}\n')

    def write_label(self, label: str) -> None:
        """
        Writes a VM 'label' command
        Args:
            label (str) -
        Returns: None
        """
        self.out_file.write(f'label {label}\n')

    def write_goto(self, label: str) -> None:
        """
        Writes a VM 'goto' command
        Args:
            label (str) -
        Returns: None
        """
        self.out_file.write(f'goto {label}\n')

    def write_if(self, label: str) -> None:
        """
        Writes a VM 'if' command
        Args:
            label (str) -
        Returns: None
        """
        self.out_file.write(f'if-goto {label}\n')

    def write_call(self, name: str, n_args: int, class_name: str = None) -> None:
        """
        Writes a VM 'call' command
        Args:
            name (str) -
            n_args (int) -
        Returns: None
        """
        if class_name:
            self.out_file.write(f'call {class_name}.{name} {n_args}\n')
        else:
            self.out_file.write(f'call {name} {n_args}\n')

    def write_function(self, name: str, l_locals: int, class_name: str = None) -> None:
        """
        Writes a VM 'function' command
        Args:
            name (str) -
            l_locals (int) -
        Returns: None
        """
        if class_name:
            self.out_file.write(f'function {class_name}.{name} {l_locals}\n')
        else:
            self.out_file.write(f'function {name} {l_locals}\n')

    def write_integerConst(self, const: int = 0):
        """
       Writes a VM 'push const' command
        Args:
            const (int) - const to be pushed
        Returns: None
        """
        self.out_file.write(f'push constant {const}\n')

    def write_string(self, stringConstant: str) -> None:
        """

        """
        # Initialize new String object (invokes OS String.new)
        self.write_push('constant', len(stringConstant))
        self.write_call("String.new", 1)
        # Builds the string (invokes OS String.appendChar)
        for c in stringConstant:
            self.write_push("constant", ord(c))
            self.write_call("String.appendChar", 2)

    def write_return(self) -> None:
        """
        Writes a VM 'return' command
        Returns: None
        """
        self.out_file.write('return\n')

    def close(self) -> None:
        """
        Close the output file
        Returns: None
        """
        pass
