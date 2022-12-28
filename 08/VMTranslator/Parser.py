from Command import Command


class Parser(object):
    """
    Performs parsing of a single .vm file, and encapsulates access to the input code.
    Reads Prog.vm file line-by-line skips empty or comments lines, when encounters a valid VM Command,
    It creates Command object which provides convenient and safe access to command's components.
    """
    def __init__(self, vm_file: str):
        self._current_command = None
        self._file_iterator = open(vm_file, 'r')
        self._commands_parsed = 0

    def has_more_commands(self) -> bool:
        """
        Returns: True if there are more commands in the input, False else.
        """
        cursor = self._file_iterator.tell()
        has_more_line = bool(self._file_iterator.readline())
        self._file_iterator.seek(cursor)
        return has_more_line

    def advance(self) -> None:
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if hasMoreCommands() is True. Initially there is no current command.
        Note that advance skips empty lines and comment lines. it also removes in-line comments.
        Returns: None.
        """
        while self.has_more_commands():
            in_command = self._file_iterator.readline().split("//")[0].strip()
            if len(in_command) > 0 and not in_command.startswith("\n"):
                self._current_command = Command(in_command)
                self._commands_parsed += 1
                break

    def get_current_command(self) -> Command:
        """
        Returns: (Command) current command object
        """
        return self._current_command

    def get_lines_parsed(self) -> int:
        """
        Returns: the number of VM code lines Parsed by Parser
        """
        return self._commands_parsed if self._commands_parsed else 1

    def close(self) -> None:
        """
        Close the file iterator stream
        """
        self._file_iterator.close()
