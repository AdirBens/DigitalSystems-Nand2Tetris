
class CodeWriter(object):

    """
    Translates VM commands into Hack assembly code
    """

    def __init__(self, input_file: str):
        self.input_file = input_file
        self.output_file = open(output, 'w')

    def set_file_name(self, file_name: str) -> None:
        """
        Informs the code writer that the translation of a new VM file is started
        :param file_name:
        :return: None
        """
        self.output_file = open(output, 'w')


    def write_arithmetic(self, command: str, count: str) -> None:
        """
        Writes the assembly code that is the translation of the given arithmetic command
        :param command: A Valid Arithmetic command ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')
        :param count: counter for true/false/continue reference

        :return: newLine: New line to be added
        """
        newline = None
        false = '@FALSE' + count
        true = '@TRUE' + count

        if command == 'add':
            newline = ['// ADD operator: '] + self.two_last() + ['M=M+D', '@SP', 'M=M+1']
        elif command == 'sub':
            newline = ['// SUB operator: '] + self.two_last() + ['M=M-D', '@SP', 'M=M+1']
        elif command == 'neg':
            newline = ['// NEG operator: ', '@SP', 'M=M-1', 'A=M', 'M=-M', '@SP', 'M=M+1']
        elif command == 'eq':
            newline = ['// EQ operator: '] + self.two_last() + ['D=D-M', false, 'D;JNE', true, 'D;JEQ'] \
                      + self.true_false(count)
        elif command == 'lt':
            newline = ['// LT operator: '] + self.two_last() + \
                      ['D=D-M', false, 'D;JLE', true, 'D;JGT'] + self.true_false(count)
        elif command == 'gt':
            newline = ['// GT operator: '] + self.two_last() + \
                      ['D=D-M', false, 'D;JGE', true, 'D;JEQ'] + self.true_false(count)
        elif command == 'and':
            newline = ['// AND operator: '] + self.two_last() + ['M=D&M', '@SP', 'M=M+1']
        elif command == 'or':
            newline = ['// OR operator: '] + self.two_last() + ['M=D|M', '@SP', 'M=M+1']
        elif command == 'not':
            newline = ['// NOT operator: ', '@SP', 'M=M-1', 'A=M', 'M=!M', '@SP', 'M=M+1']

        self.output_file.write('\n' + '\n'.join(newline) + '\n')

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """
        Writes the assembly code that is the translation of the given command, where command is either C_PUSH or C_POP
        All the memory segments are accessed by the same two commands:
            (*) push segment index Push the value of segment[index] onto the stack
            (*) pop segment index Pop the top stack value and store it in segment[index]
        :param command: one of two commands - push, pop
        :param segment: VM `MemorySegment` to be access. Should be one of the eight segment names
                        'argument', 'loca', 'static', 'constant', 'this', 'that', 'pointer', 'temp'
        :param index: A non-negative integer represents the `index` on the Memory-segment to be access
        :return: None
        """

        newline = None
        if segment == 'constant':
            newline = ['// PUSH CONST operator:', '@' + str(index),
                       'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        elif segment == 'local':
            if command == 'pop':
                newline = self. \
                    generic_pop('LCL', index)
            else:
                newline = self.generic_push('LCL', index)

        elif segment == 'argument':
            if command == 'pop':
                newline = self.generic_pop('ARG', index)
            else:
                newline = self.generic_push('ARG', index)

        elif segment == 'this':
            if command == 'pop':
                newline = self.generic_pop('THIS', index)
            else:
                newline = self.generic_push('THIS', index)

        elif segment == 'that':
            if command == 'pop':
                newline = self.generic_pop('THAT', index)
            else:
                newline = self.generic_push('THAT', index)

        elif segment == 'temp':
            if command == 'pop':
                newline = ['// POP ' + segment + ' operator:', '@' + index, 'D=A', '@5', 'D=D+A', '@R13', 'M=D',
                           '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D', '@R13', 'M=0']
            else:
                newline = ['// PUSH ' + segment + ' operator:', '@' + index, 'D=A', '@5', 'A=D+A', 'D=M', '@SP',
                           'A=M', 'M=D', '@SP', 'M=M+1']

        elif segment == 'pointer':
            if index == '0':  # POP/PUSH THIS
                if command == 'pop':
                    newline = ['// POP ' + segment + ' operator:', '@SP', 'M=M-1', 'A=M', 'D=M', '@THIS', 'M=D']
                else:
                    newline = ['// PUSH ' + segment + ' operator:', '@THIS', 'D=M', '@SP', 'A=M', 'M=D', '@SP',
                               'M=M+1']
            else:
                if command == 'pop':  # POP/PUSH THAT
                    newline = ['// POP ' + segment + ' operator:', '@SP', 'M=M-1', 'A=M', 'D=M', '@THAT', 'M=D']
                else:
                    newline = ['// PUSH ' + segment + ' operator:', '@THAT', 'D=M', '@SP', 'A=M', 'M=D', '@SP',
                               'M=M+1']

        elif segment == 'static':
            filename = os.path.basename(path)[:-2]
            if command == 'pop':
                newline = ['// POP static operator:', '@SP', 'M=M-1', 'A=M', 'D=M',
                           '@' + filename + index, 'M=D']
            else:
                newline = ['// PUSH static operator:', '@' + filename + index,
                           'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']

        self.newfile.write('\n' + '\n'.join(newline) + '\n')

    # Generic assembly sequence that stores the two last values in the stack in D and M
    @staticmethod
    def two_last():
        return ['@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'M=M-1', 'A=M']

    # Generic assembly sequence that creates new TRUE and FALSE values and
    @staticmethod
    def true_false(index:str):
        return ['(TRUE' + str(index) + ')', '@SP', 'A=M', 'M=-1', '@CONTINUE' + str(index), 'D;JMP',
                '(FALSE' + str(index) + ')', '@SP', 'A=M', 'M=0', '@CONTINUE' + str(index), 'D;JMP',
                '(CONTINUE' + str(index) + ')', '@SP', 'M=M+1']


    # Generic POP sequence modified by given address incrementation and memory segment
    @staticmethod
    def generic_pop(segment: str, index: int):
        return ['// POP ' + segment + ' operator:', '@' + str(index), 'D=A', '@' + segment, 'D=D+M', '@R13', 'M=D',
                '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D', '@R13', 'M=0']


    # Generic PUSH sequence modified by given address incrementation and memory segment
    @staticmethod
    def generic_push(segment: str, index: int):
        return ['// PUSH ' + segment + ' operator:', '@' + index, 'D=A', '@' + segment, 'A=D+M', 'D=M', '@SP',
                'A=M', 'M=D', '@SP', 'M=M+1']