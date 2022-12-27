import os.path

from Command import Command
from MachineLanguage import MachineLanguage
from os import path


class CodeWriter(object):
    """
    Translate VM Commands into HackAssembly Code according to Machine's Standard-Mapping
    """
    def __init__(self, file_name: str):
        self._asm = MachineLanguage()
        self._templates = self._load_base_templates()
        self._standard_mapping = self.load_std_mapping()
        self._output_file = open(file_name.replace('.vm', '.asm'), 'w')
        self._base_name = path.basename(self._output_file.name)[:-4]
        self._conditions_counter = 1
        self._asm_lines_written = 0
        self._in_function = []

    def set_file_name(self, file_name: str) -> None:
        """
        Informs the code writer that the translation of a new VM file is started
        Args: file_name (str) - the name of the new file
        Returns: None.
        """
        self._base_name = file_name.split('/')[-1].split(".")[0]

    def write_arithmetic(self, command: Command) -> None:
        """
        Produces and Writes the assembly code that is the translation of the given arithmetic command
        Args:
            command (Command): A Valid Arithmetic command ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')
        Returns: None.
        """
        cmd_str = self._templates[command.arg1][command.command_type].format(counter=self._conditions_counter)
        self._conditions_counter += 1
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")

    def write_push_pop(self, command: Command) -> None:
        """
        Produces and Writes the assembly code that is the translation of the given command,
        where command is either C_PUSH or C_POP. All the memory segments are accessed by the same two commands:
            (*) push segment index Push the value of segment[index] onto the stack
            (*) pop segment index Pop the top stack value and store it in segment[index]
        Args: command (Command): command object
        Returns: None.
        """
        cmd_str = self._templates[command.arg1][command.command_type].format(
            segment=self._standard_mapping[command.arg1],
            index=str(command.arg2),
            file=self._base_name)
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")

    def write_init(self) -> None:
        """
        Writes assembly code that effects the VM initialization, also called bootstrap code.
        This code must be placed at the beginning of the output ﬁle.
        Returns: None.
        """
        command = Command("call Sys.init 0")
        cmd_str = self._templates['init']['SYS_INIT']
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self.write_call(command)
        self._asm_lines_written += cmd_str.count("\n")

    def write_label(self, command: Command) -> None:
        """
        Writes assembly code that effects the `label` command.
        Args: label (str) - string represents the label
        Returns: None.
        """
        label = "{}${}".format(self._in_function[-1], command.arg1) if len(self._in_function) else command.arg1
        cmd_str = self._templates[command.operation][command.command_type].format(label=label)
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")

    def write_goto(self, command: Command) -> None:
        """
        Writes assembly code that effects the `goto` command.
        Args: label (str) - string represents the label
        Returns: None.
        """
        cmd_str = self._templates[command.operation][command.command_type].format(dest=command.arg1)
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")

    def write_if(self, command: Command) -> None:
        """
        Writes assembly code that effects the `if-goto` command.
        Args: label (str) - string represents the label
        Returns: None.
        """
        self.write_goto(command)

    def write_call(self, command: Command) -> None:
        """
        Writes assembly code that effects the `call` command.
        Args:
            function_name (str) - the name of the callee function
            num_args (int) - the number of arguments the callee function takes
        Returns: None.
        """
        # TODO: Implement CodeWriter.write_call
        cmd_str = self._templates[command.operation][command.command_type].format(function_name=command.arg1,
                                                                                  num_args=command.arg2)
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")

    def write_return(self, command: Command) -> None:
        """
        Writes assembly code that effects the `return` command.
        Returns: None.
        """
        # TODO: Implement CodeWriter.write_return
        cmd_str = self._templates[command.operation][command.command_type]
        self._output_file.write(self._comment_code_block(command, cmd_str))
        self._asm_lines_written += cmd_str.count("\n")
        self._in_function.pop()

    def write_function(self, command: Command) -> None:
        """
        Writes assembly code that effects the `function` command.
        Args:
            function_name (str) - the name of the function been called
            num_locals (int) - the number of function's local variables
        Returns: None.
        :param command:
        """
        self._in_function.append(command.arg1)
        cmd_str = self._templates[command.operation][command.command_type].format(function_name=command.arg1)
        cmd_str += command.arg2 * (self._asm.PushD + "\n")
        self._output_file.write(self._comment_code_block(command, cmd_str[:-2]))
        self._asm_lines_written += cmd_str.count("\n")

    def get_lines_produced(self) -> int:
        """
        Returns: the number of Assembly code lines produced by CodeWriter
        """
        return self._asm_lines_written

    def close(self) -> None:
        """
        Close output file stream
        """
        self._output_file.close()

    @staticmethod
    def _comment_code_block(cmd: Command, codeblock: str) -> str:
        """
        Append Comment on produces asm code block
        Args:
            cmd (Command) - the command object which asm code produced from
            codeblock (str) - the asm codeblock produced from the command
        Returns: (str) commented code block
        """
        return "\n".join(['', '// For VM Command {}', '//  Produce {} ASM CodeBlock', codeblock]).format(cmd.__str__(),
                                                                                                         cmd.command_type)

    @staticmethod
    def load_std_mapping() -> dict:
        """
        Returns: dictionary represents Machine Standard-Memory Mapping
        """
        return {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
            'pointer': 3,
            'temp': 5,
            'static': 16,
            'constant': '',
        }

    def _load_base_templates(self) -> dict:
        """
        Returns: Dictionary Holds HackAssembly Command's base templates
        """
        return {
            # Stack Operations Corresponds MemorySegment
            'argument': {"C_PUSH": self._asm.PUSH_SEGMENT, "C_POP": self._asm.POP_SEGMENT},
            'local': {"C_PUSH": self._asm.PUSH_SEGMENT, "C_POP": self._asm.POP_SEGMENT},
            'this': {"C_PUSH": self._asm.PUSH_SEGMENT, "C_POP": self._asm.POP_SEGMENT},
            'that': {"C_PUSH": self._asm.PUSH_SEGMENT, "C_POP": self._asm.POP_SEGMENT},
            'constant': {"C_PUSH": self._asm.PUSH_CONST, "C_POP": None},
            'temp': {"C_PUSH": self._asm.PUSH_TEMP, "C_POP": self._asm.POP_TEMP},
            'pointer': {"C_PUSH": self._asm.PUSH_POINTER, "C_POP": self._asm.POP_POINTER},
            'static': {"C_PUSH": self._asm.PUSH_STATIC, "C_POP": self._asm.POP_STATIC},
            # Arithmetic Operations
            'add': {"C_ARITHMETIC": self._asm.ADD},
            'sub': {"C_ARITHMETIC": self._asm.SUB},
            'and': {"C_ARITHMETIC": self._asm.AND},
            'or': {"C_ARITHMETIC": self._asm.OR},
            'neg': {"C_ARITHMETIC": self._asm.NEG},
            'not': {"C_ARITHMETIC": self._asm.NOT},
            'eq': {"C_ARITHMETIC": self._asm.EQ},
            'gt': {"C_ARITHMETIC": self._asm.GT},
            'lt': {"C_ARITHMETIC": self._asm.LT},

            #Branching Operations
            'label': {"C_LABEL": self._asm.LABEL},
            'goto': {"C_GOTO": self._asm.GOTO},
            'if_goto': {"C_IF": self._asm.IF},
            'call': {"C_CALL": self._asm.CALL},
            'function': {"C_FUNCTION": self._asm.FUNCTION},
            'return': {"C_RETURN": self._asm.RETURN},
            'init': {"SYS_INIT": self._asm.INIT}
            #TODO: goto is in if-goto !!!!!!!
        }
