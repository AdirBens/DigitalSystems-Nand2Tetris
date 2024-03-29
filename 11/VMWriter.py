class VMWriter(object):
    """
    Emits VM commands into a file, using the VM command syntax.
    """
    def __init__(self, out=None):
        """
        Creates a new VMWriter, set out file and prepares it for writing.
        """
        self.out_file = out

    def set_outfile(self, out_file) -> None:
        self.out_file = out_file

    def write_push(self, segment: str, index: int) -> None:
        """
        Writes a VM push command
        Args: segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
                index (int) - offset on this memory segment
        """
        segment = {'field': 'this', 'arg': 'argument', 'var': 'local'}.get(segment, segment)
        self.out_file.write(f'push {segment} {index}\n')

    def write_pop(self, segment: str, index: int) -> None:
        """
        Writes a VM pop command
        Args: segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
                index (int) - offset on this memory segment
        """
        segment = {'field': 'this', 'arg': 'argument', 'var': 'local'}.get(segment, segment)
        self.out_file.write(f'pop {segment} {index}\n')

    def write_arithmetic(self, command: str, op_type: str = "binary") -> None:
        """
        Writes a VM arithmetic command
        Args: command (str) - ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
        """
        ops = {"binary": {'+': 'add', '-': 'sub', '*': 'call Math.multiply 2', '/': 'call Math.divide 2',
                          '&amp;': 'and', '|': 'or', '&lt;': 'lt', '&gt;': 'gt', '=': 'eq'},
               "unary": {'~': 'not', '-': 'neg'}}
        self.out_file.write(f'{ops.get(op_type).get(command)}\n')

    def write_label(self, label: str, index: int = -1) -> None:
        """
        Writes a VM 'label' command
        Args: label (str) - The label to write
              [OPTIONAL] index (int) - index or counter
        """
        index = "" if index == -1 else str(index)
        self.out_file.write(f'label {label}{index}\n')

    def write_goto(self, label: str) -> None:
        """
        Writes a VM 'goto' command
        Args: label (str) - The label to write
        """
        self.out_file.write(f'goto {label}\n')

    def write_if(self, label: str, is_neg: bool = False) -> None:
        """
        Writes a VM 'if' command
        Args: label (str) - The label to write
              [OPTIONAL; default False] is_neg (bool) - write negate if.
        """
        if is_neg:
            self.write_arithmetic("~", op_type='unary')
        self.out_file.write(f'if-goto {label}\n')

    def write_call(self, name: str, n_args: int, class_name: str = None) -> None:
        """
        Writes a VM 'call' command
        Args: name (str) - subroutine name
            n_args (int) - number of args called subroutine gets
            [OPTIONAL; default None] class_name (str) - name of subroutines parent class
        """
        if class_name:
            self.out_file.write(f'call {class_name}.{name} {n_args}\n')
        else:
            self.out_file.write(f'call {name} {n_args}\n')

    def write_function(self, name: str, l_locals: int, class_name: str = None) -> None:
        """
        Writes a VM 'function' command
        Args:     name (str) - function name
              l_locals (int) - number of function's local variables
              [OPTIONAL; default None] class_name (str) - name of functions parent class
        """
        if class_name:
            self.out_file.write(f'function {class_name}.{name} {l_locals}\n')
        else:
            self.out_file.write(f'function {name} {l_locals}\n')

    def write_integer_const(self, const: int = 0):
        """
        Writes a VM 'push const' command
        Args: const (int) - integer const to be pushed
        """
        self.out_file.write(f'push constant {const}\n')

    def write_string(self, string_constant: str) -> None:
        """
        Writes a String as a sequence of chars on const memory segment.
        Invokes System built-in functions - String.new(), String.appendChar()
        Args: string_constant (str) - the string to write
        """
        # Initialize new String object (invokes OS String.new)
        self.write_push(segment='constant', index=len(string_constant))
        self.write_call(name="String.new", n_args=1)
        # Builds the string (invokes OS String.appendChar)
        for c in string_constant:
            self.write_push(segment="constant", index=ord(c))
            self.write_call(name="String.appendChar", n_args=2)

    def write_return(self) -> None:
        """
        Writes a VM 'return' command
        """
        self.out_file.write('return\n')
