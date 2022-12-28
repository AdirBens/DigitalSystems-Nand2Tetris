
// -------------------------- Wed Dec 28 22:26:13 2022 --------------------------
// VMTranslation Session - Translation of FibonacciSeries.vm to HackAssembly code.
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  29 VM Code lines parsed.
//      [+] VMTranslator:  222 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 7.655172413793103 has been reached.
// ------------------------------------------------------------------------------


// For VM Command push argument 1
//  Produce C_PUSH ASM CodeBlock
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop pointer 1
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@THAT
M=D

// For VM Command push constant 0
//  Produce C_PUSH ASM CodeBlock
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop that 0
//  Produce C_POP ASM CodeBlock
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command push constant 1
//  Produce C_PUSH ASM CodeBlock
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop that 1
//  Produce C_POP ASM CodeBlock
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command push argument 0
//  Produce C_PUSH ASM CodeBlock
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push constant 2
//  Produce C_PUSH ASM CodeBlock
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command sub
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

// For VM Command pop argument 0
//  Produce C_POP ASM CodeBlock
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command label MAIN_LOOP_START
//  Produce C_LABEL ASM CodeBlock
(MAIN_LOOP_START)

// For VM Command push argument 0
//  Produce C_PUSH ASM CodeBlock
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command if-goto COMPUTE_ELEMENT
//  Produce C_IF ASM CodeBlock
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE

// For VM Command goto END_PROGRAM
//  Produce C_GOTO ASM CodeBlock
@END_PROGRAM
0;JMP

// For VM Command label COMPUTE_ELEMENT
//  Produce C_LABEL ASM CodeBlock
(COMPUTE_ELEMENT)

// For VM Command push that 0
//  Produce C_PUSH ASM CodeBlock
@THAT
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push that 1
//  Produce C_PUSH ASM CodeBlock
@THAT
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command add
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

// For VM Command pop that 2
//  Produce C_POP ASM CodeBlock
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command push pointer 1
//  Produce C_PUSH ASM CodeBlock
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push constant 1
//  Produce C_PUSH ASM CodeBlock
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command add
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

// For VM Command pop pointer 1
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@THAT
M=D

// For VM Command push argument 0
//  Produce C_PUSH ASM CodeBlock
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push constant 1
//  Produce C_PUSH ASM CodeBlock
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command sub
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

// For VM Command pop argument 0
//  Produce C_POP ASM CodeBlock
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command goto MAIN_LOOP_START
//  Produce C_GOTO ASM CodeBlock
@MAIN_LOOP_START
0;JMP

// For VM Command label END_PROGRAM
//  Produce C_LABEL ASM CodeBlock
(END_PROGRAM)
