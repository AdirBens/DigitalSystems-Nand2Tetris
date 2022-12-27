
class MachineLanguage(object):
    """
    Holds MachineLanguage Assembly Common Routines base Templates
    """
    def __init__(self):
        # Common Routines
        push_d = "\n".join(['@SP', 'A=M', 'M=D', '@SP', 'M=M+1'])
        pop_d = "\n".join(['@SP', 'AM=M-1', 'D=M'])
        inc_sp = "\n".join(['@SP', 'M=M+1'])
        symbol_false = "\n".join(['@FALSE{counter}'])
        symbol_true = "\n".join(['@TRUE{counter}'])
        bool_labels = "\n".join(['(TRUE{counter})', '@SP', 'A=M', 'M=-1', '@CONTINUE{counter}', 'D;JMP',
                                 '(FALSE{counter})', '@SP', 'A=M', 'M=0', '@CONTINUE{counter}', 'D;JMP',
                                 '(CONTINUE{counter})', '@SP', 'M=M+1'])
        label = "\n".join([])


        self._line_seperator()
        self.__dict__.update({
        # Update MachineLanguage Dict with Commands Base Templates
        # ------------------------------------------------------------------------------------------------------------
          # Common Routines
            'PopD': ['@SP', 'AM=M-1', 'D=M'],
            'PopDTwice': ['@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1'],
            'PushD': ['@SP', 'A=M', 'M=D', '@SP', 'M=M+1'],
            'Inc_SP': ['@SP', 'M=M+1'],
          # StackOperations Templates According MemorySegments
          # ----------------------------------------------------------------------------------------------------------
            # C_POP
            'POP_SEGMENT': ['@{index}', 'D=A', '@{segment}', 'D=D+M', '@R13', 'M=D', pop_d, '@R13', 'A=M', 'M=D'],
            'POP_STATIC': [pop_d, '@{file}.{index}', 'M=D'],
            'POP_TEMP': ['@{segment}', 'D=A', '@{index}', 'D=D+A', '@R13', 'M=D', pop_d, '@R13', 'A=M', 'M=D'],
            'POP_POINTER': [pop_d, '@{index}', 'M=D'],
            # C_PUSH
            'PUSH_SEGMENT': ['@{index}', 'D=A', '@{segment}', 'A=D+M', 'D=M', push_d],
            'PUSH_STATIC': ['@{file}.{index}', 'D=M', push_d],
            'PUSH_TEMP': ['@{index}', 'D=A', '@{segment}', 'A=D+A', 'D=M', push_d],
            'PUSH_POINTER': ['@{index}', 'D=M', push_d],
            'PUSH_CONST': ['@{index}', 'D=A', push_d],
          # ARITHMETIC
          # ----------------------------------------------------------------------------------------------------------
            'ADD': [pop_d, pop_d[:-4], "M=M+D", inc_sp],
            'SUB': [pop_d, pop_d[:-4], "M=M-D", inc_sp],
            'AND': [pop_d, pop_d[:-4], "M=M&D", inc_sp],
            'OR': [pop_d, pop_d[:-4], "M=M|D", inc_sp],
            'EQ': [pop_d, pop_d[:-4], "D=M-D", symbol_false, "D;JNE", symbol_true, "D;JEQ", bool_labels],
            'GT': [pop_d, pop_d[:-4], "D=M-D", symbol_false, "D;JLE", symbol_true, "D;JGT", bool_labels],
            'LT': [pop_d, pop_d[:-4], "D=M-D", symbol_false, "D;JGE", symbol_true, "D;JLT", bool_labels],
            'NEG': [pop_d, "M=-M", inc_sp],
            'NOT': [pop_d, "M=!M", inc_sp],
          # Branching
          # ----------------------------------------------------------------------------------------------------------
            # INIT (BOOTSTRAP)
            'INIT': ['@256', 'D=A', '@SP', 'M=D'],
            # LABEL
            'LABEL': ['({label})'],
            # GOTO
            'GOTO': ['@{dest}', 'D;JMP'],
            # IF-GOTO
            'IF': [pop_d, '@{dest}', 'D;JNE'],
            # CALL
            'CALL': ['@{function_name}_return_address{label_counter}', 'D=A', push_d,
                     '@LCL', 'D=M', push_d,
                     '@ARG', 'D=M', push_d,
                     '@THIS', 'D=M', push_d,
                     '@THAT', 'D=M', push_d,
                     '@5', 'D=A', '@{num_args}', 'D=A-D', '@SP', 'D=M-D', '@ARG', 'M=D',
                     '@SP', 'D=M', '@LCL', 'M=D',
                     '@{function_name}', 'D;JMP',
                     '({function_name}_return_address{label_counter})'],
            # FUNCTION
            'FUNCTION': ['({function_name})', 'D=0'],
            # RETURN
            'RETURN': ['@LCL', 'D=M', '@FRAME', 'M=D',
                       '@5', 'A=D-A', 'D=M', '@FRAME', 'M=D', '@RET', 'M=D',
                       pop_d, '@ARG', 'A=M', 'M=D',
                       'D=M+1', '@SP', 'M=D',
                       '@FRAME', 'DAM=M-1', 'D=M', '@THAT', 'M=D',
                       '@FRAME', 'DAM=M-1', 'D=M', '@THIS', 'M=D',
                       '@FRAME', 'DAM=M-1', 'D=M', '@ARG', 'M=D',
                       '@FRAME', 'DAM=M-1', 'D=M', '@LCL', 'M=D',
                       '@RET', 'A=M', 'D;JMP'
                       ]
        })

    def _line_seperator(self) -> None:
        """
        Assemble commands components into a format-able strings.
        """
        for k in self.__dict__.keys():
            self.__dict__[k] = "\n".join(self.__dict__[k]) + "\n"