# DO NOT TOUCH - PROJECT 11

class VMWriter(object):
    """
    Emits VM commands into a file, using the VM command syntax.
    """

    def __init__(self, out: str):
        """
        Creates a new VMWriter, set out file and prepares it for writing.
        """
        pass

    def write_push(self, segment: str, index: int) -> None:
        """
        Writes a VM push command
        Args:
            segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
            index (int) -
        Returns: None
        """
        pass

    def write_pop(self, segment: str, index: int) -> None:
        """
        Writes a VM pop command
        Args:
            segment (str) - CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
            index (int) -
        Returns: None
        """
        pass

    def write_arithmetic(self, command: str) -> None:
        """
        Writes a VM arithmetic command
        Args:
            command (str) - ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
        :Returns: None
        """
        pass

    def write_label(self, label: str) -> None:
        """
        Writes a VM 'label' command
        Args:
            label (str) -
        Returns: None
        """
        pass

    def write_goto(self, label: str) -> None:
        """
        Writes a VM 'goto' command
        Args:
            label (str) -
        Returns: None
        """
        pass

    def write_if(self, label: str) -> None:
        """
        Writes a VM 'if' command
        Args:
            label (str) -
        Returns: None
        """
        pass

    def write_call(self, name: str, n_args: int) -> None:
        """
        Writes a VM 'call' command
        Args:
            name (str) -
            n_args (int) -
        Returns: None
        """
        pass

    def write_function(self, name: str, l_locals: int) -> None:
        """
        Writes a VM 'function' command
        Args:
            name (str) -
            l_locals (int) -
        Returns: None
        """
        pass

    def write_return(self) -> None:
        """
        Writes a VM 'return' command
        Returns: None
        """
        pass

    def close(self) -> None:
        """
        Close the output file
        Returns: None
        """
        pass
