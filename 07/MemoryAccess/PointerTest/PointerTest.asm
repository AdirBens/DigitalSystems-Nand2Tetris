
// ------------------------Mon Dec 26 22:42:26 2022------------------------
// VMTranslator - Translation Of PointerTest.vm to HackAssembly code.
//  [+] Translation end successfully.
//      [>] 15 VM Code lines parsed
//      [>] 120 ASM Code lines produced.
//      [>] Translation ratio is 8.0
// ------------------------------------------------------------------------

// For VM Command push constant 3030
//  Produce C_PUSH ASM CodeBlock
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop pointer 0
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@THIS
M=D
// For VM Command push constant 3040
//  Produce C_PUSH ASM CodeBlock
@3040
D=A
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
// For VM Command push constant 32
//  Produce C_PUSH ASM CodeBlock
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop this 2
//  Produce C_POP ASM CodeBlock
@2
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
// For VM Command push constant 46
//  Produce C_PUSH ASM CodeBlock
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop that 6
//  Produce C_POP ASM CodeBlock
@6
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
// For VM Command push pointer 0
//  Produce C_PUSH ASM CodeBlock
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push pointer 1
//  Produce C_PUSH ASM CodeBlock
@THAT
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
// For VM Command push this 2
//  Produce C_PUSH ASM CodeBlock
@2
D=A
@THIS
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
// For VM Command push that 6
//  Produce C_PUSH ASM CodeBlock
@6
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
