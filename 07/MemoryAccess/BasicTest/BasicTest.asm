
// ------------------------Mon Dec 26 22:42:18 2022------------------------
// VMTranslator - Translation Of BasicTest.vm to HackAssembly code.
//  [+] Translation end successfully.
//      [>] 25 VM Code lines parsed
//      [>] 233 ASM Code lines produced.
//      [>] Translation ratio is 9.32
// ------------------------------------------------------------------------

// For VM Command push constant 10
//  Produce C_PUSH ASM CodeBlock
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop local 0
//  Produce C_POP ASM CodeBlock
@0
D=A
@LCL
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command push constant 21
//  Produce C_PUSH ASM CodeBlock
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 22
//  Produce C_PUSH ASM CodeBlock
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop argument 2
//  Produce C_POP ASM CodeBlock
@2
D=A
@ARG
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command pop argument 1
//  Produce C_POP ASM CodeBlock
@1
D=A
@ARG
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command push constant 36
//  Produce C_PUSH ASM CodeBlock
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop this 6
//  Produce C_POP ASM CodeBlock
@6
D=A
@THIS
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command push constant 42
//  Produce C_PUSH ASM CodeBlock
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 45
//  Produce C_PUSH ASM CodeBlock
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop that 5
//  Produce C_POP ASM CodeBlock
@5
D=A
@THAT
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command pop that 2
//  Produce C_POP ASM CodeBlock
@2
D=A
@THAT
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command push constant 510
//  Produce C_PUSH ASM CodeBlock
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop temp 6
//  Produce C_POP ASM CodeBlock
@5
D=A
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// For VM Command push local 0
//  Produce C_PUSH ASM CodeBlock
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push that 5
//  Produce C_PUSH ASM CodeBlock
@5
D=A
@THAT
A=D+M
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
// For VM Command push argument 1
//  Produce C_PUSH ASM CodeBlock
@1
D=A
@ARG
A=D+M
D=M
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
// For VM Command push this 6
//  Produce C_PUSH ASM CodeBlock
@6
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push this 6
//  Produce C_PUSH ASM CodeBlock
@6
D=A
@THIS
A=D+M
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
// For VM Command push temp 6
//  Produce C_PUSH ASM CodeBlock
@6
D=A
@5
A=D+A
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
