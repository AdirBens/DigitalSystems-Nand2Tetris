

class Parser(object):
    """
    Handles the parsing of a single .vm file, and encapsulates access to the input code.
    It reads VM commands, parses them, and provides convenient access to their components.
    In addition, it removes all white space and comments.
    """

    ARITH_ACTIONS = {'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'}
    PP_ACTIONS = {'push', 'pop'}

    def __init__(self, vm_file: str):
        self.f = open(vm_file, 'r')
        self.current_command = None


    def has_more_commands(self) -> bool:
        """
        :return: True if there are more commands in the input, False else.
        """
        self.advance()
        while self.current_command != '/n' or self.current_command != '':
            return True
        else:
            return False

                self.line_list.append(line.split())
        f.close()


    def advance(self) -> None:
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if hasMoreCommands() is True. Initially there is no current command.
        :return: None
        """
        cur_line = self.f.readline()
        while cur_line != None:
            cur_line = ''.split(cur_line)
            if cur_line[0] is not in self.ARITH



    def command_type(self) -> str:
        """
        :return: The type of the current VM command.
        C_ARITHMETIC is returned for all the arithmetic commands.
        """
        pass


    def arg1(self) -> str:
        """
        :return: The first argument of the current command.
        In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
        Should not be called if the current command is C_RETURN.
        """
        if not self.current_command == 'C_RETURN':
            pass


    def arg2(self) -> int:
        """
        :return: The second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        """
        if self.current_command in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            pass



class Parser:

    def __init__(self):
        self.path = sys.argv[1]
        self.line_list = []
        self.trans_list = []
        output = self.path[:-3] + ".asm"
        self.newfile = open(output, 'w')

    # Creates a list from the text in the given file
    def file_to_list(self):
        f = open(self.path, 'r')
        for line in f.readlines():
            if line != '/n' or line != '':
                self.line_list.append(line.split())
        f.close()

    # Translates the list calling other methods according to the command type
    def list_to_trans_list(self):
        count_true_false = 0
        for line in self.line_list:
            if len(line) == 0:
                continue
            else:
                if line[0] in arith_actions:
                    count_true_false += 1
                    newline = CodeWriter.arith_trans(line, count_true_false)
                    self.trans_list.append(newline)
                elif line[0] in pp_actions:
                    newline = self.pp_trans(line, self.path)
                    self.trans_list.append(newline)
        print(self.trans_list)


    def hasMoreCommands:
