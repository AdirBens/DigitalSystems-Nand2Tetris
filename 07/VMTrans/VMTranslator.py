import sys
import os.path

""" VMTranslator translates from jack code to assembly code and is part of the Nand2Tetris part 2 course.
    Given a file name xxx.vm as parameter the file creates a new file with the same name ending with .asm."""


arith_actions = {'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'}
pp_actions = {'push', 'pop'}


class VMTrans:

    def __init__(self):
        self.path = sys.argv[1]
        self.line_list = []
        self.trans_list = []
        output = self.path[:-3] + ".asm"
        self.newfile = open(output, 'w')

    # Main runs all corresponding functions
    def main(self):
        self.file_to_list()
        self.list_to_trans_list()
        self.write()

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
                    newline = self.arith_trans(line, count_true_false)
                    self.trans_list.append(newline)
                elif line[0] in pp_actions:
                    newline = self.pp_trans(line, self.path)
                    self.trans_list.append(newline)
        print(self.trans_list)

    # Writes to the output file and closes it after writing
    def write(self):
        for line in self.trans_list:
            self.newfile.write('\n' + '\n'.join(line) + '\n')
        self.newfile.close()

    # Translates arithmatic single command to assembly code
    def arith_trans(self, line, count):
        newline = None
        count = str(count)
        false = '@FALSE' + count
        true = '@TRUE' + count

        if line[0] == 'add':
            newline = ['// ADD operator: '] + self.two_last() + ['M=M+D', '@SP', 'M=M+1']
        elif line[0] == 'sub':
            newline = ['// SUB operator: '] + self.two_last() + ['M=M-D', '@SP', 'M=M+1']
        elif line[0] == 'neg':
            newline = ['// NEG operator: ', '@SP', 'M=M-1', 'A=M', 'M=-M', '@SP', 'M=M+1']
        elif line[0] == 'eq':
            newline = ['// EQ operator: '] + self.two_last() + ['D=D-M', false, 'D;JNE', true, 'D;JEQ'] \
                      + self.true_false(count)
        elif line[0] == 'lt':
            newline = ['// LT operator: '] + self.two_last() + \
                      ['D=D-M', false, 'D;JLE', true, 'D;JGT'] + self.true_false(count)
        elif line[0] == 'gt':
            newline = ['// GT operator: '] + self.two_last() + \
                      ['D=D-M', false, 'D;JGE', true, 'D;JEQ'] + self.true_false(count)
        elif line[0] == 'and':
            newline = ['// AND operator: '] + self.two_last() + ['M=D&M', '@SP', 'M=M+1']
        elif line[0] == 'or':
            newline = ['// OR operator: '] + self.two_last() + ['M=D|M', '@SP', 'M=M+1']
        elif line[0] == 'not':
            newline = ['// NOT operator: ', '@SP', 'M=M-1', 'A=M', 'M=!M', '@SP', 'M=M+1']
        return newline

    # Generic assembly sequence that stores the two last values in the stack in D and M
    @staticmethod
    def two_last():
        return ['@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'M=M-1', 'A=M']

    # Generic assembly sequence that creates new TRUE and FALSE values and
    @staticmethod
    def true_false(count):
        return ['(TRUE' + str(count) + ')', '@SP', 'A=M', 'M=-1', '@CONTINUE' + str(count), 'D;JMP',
                '(FALSE' + str(count) + ')', '@SP', 'A=M', 'M=0', '@CONTINUE' + str(count), 'D;JMP',
                '(CONTINUE' + str(count) + ')', '@SP', 'M=M+1']

    # Translates PUSH/POP single command to assembly code according to memory segment
    def pp_trans(self, line, path):
        newline = None
        if line[1] == 'constant':
            newline = ['// PUSH CONST operator:', '@' + line[2],
                       'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        elif line[1] == 'local':
            if line[0] == 'pop':
                newline = self.\
                    generic_pop(line, line[2], 'LCL')
            else:
                newline = self.generic_push(line, line[2], 'LCL')

        elif line[1] == 'argument':
            if line[0] == 'pop':
                newline = self.generic_pop(line, line[2], 'ARG')
            else:
                newline = self.generic_push(line, line[2], 'ARG')

        elif line[1] == 'this':
            if line[0] == 'pop':
                newline = self.generic_pop(line, line[2], 'THIS')
            else:
                newline = self.generic_push(line, line[2], 'THIS')

        elif line[1] == 'that':
            if line[0] == 'pop':
                newline = self.generic_pop(line, line[2], 'THAT')
            else:
                newline = self.generic_push(line, line[2], 'THAT')

        elif line[1] == 'temp':
            if line[0] == 'pop':
                newline = ['// POP ' + line[1] + ' operator:', '@' + line[2], 'D=A', '@5', 'D=D+A', '@R13', 'M=D',
                           '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D', '@R13', 'M=0']
            else:
                newline = ['// PUSH ' + line[1] + ' operator:', '@' + line[2], 'D=A', '@5', 'A=D+A', 'D=M', '@SP',
                           'A=M', 'M=D', '@SP', 'M=M+1']

        elif line[1] == 'pointer':
            if line[2] == '0':  # POP/PUSH THIS
                if line[0] == 'pop':
                    newline = ['// POP ' + line[1] + ' operator:', '@SP', 'M=M-1', 'A=M', 'D=M', '@THIS', 'M=D']
                else:
                    newline = ['// PUSH ' + line[1] + ' operator:', '@THIS', 'D=M', '@SP', 'A=M', 'M=D', '@SP',
                               'M=M+1']
            else:
                if line[0] == 'pop':  # POP/PUSH THAT
                    newline = ['// POP ' + line[1] + ' operator:', '@SP', 'M=M-1', 'A=M', 'D=M', '@THAT', 'M=D']
                else:
                    newline = ['// PUSH ' + line[1] + ' operator:', '@THAT', 'D=M', '@SP', 'A=M', 'M=D', '@SP',
                               'M=M+1']

        elif line[1] == 'static':
            filename = os.path.basename(path)[:-2]
            if line[0] == 'pop':
                newline = ['// POP static operator:', '@SP', 'M=M-1', 'A=M', 'D=M',
                           '@' + filename + line[2], 'M=D']
            else:
                newline = ['// PUSH static operator:', '@' + filename + line[2],
                           'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']

        return newline

    # Generic POP sequence modified by given address incrementation and memory segment
    @staticmethod
    def generic_pop(line, address_inc, mem_seg):
        return ['// POP ' + line[1] + ' operator:', '@' + address_inc, 'D=A', '@' + mem_seg, 'D=D+M', '@R13', 'M=D',
                '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D', '@R13', 'M=0']

    # Generic PUSH sequence modified by given address incrementation and memory segment
    @staticmethod
    def generic_push(line, address_inc, mem_seg):
        return ['// PUSH ' + line[1] + ' operator:', '@' + address_inc, 'D=A', '@' + mem_seg, 'A=D+M', 'D=M', '@SP',
                'A=M', 'M=D', '@SP', 'M=M+1']


if __name__ == "__main__":
    VMTrans().main()


