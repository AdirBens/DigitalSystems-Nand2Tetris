
// ------------------------Mon Dec 26 22:42:36 2022------------------------
// VMTranslator - Translation Of StaticTest.vm to HackAssembly code.
//  [+] Translation end successfully.
//      [>] 11 VM Code lines parsed
//      [>] 73 ASM Code lines produced.
//      [>] Translation ratio is 6.636363636363637
// ------------------------------------------------------------------------

// For VM Command push constant 111
//  Produce C_PUSH ASM CodeBlock
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 333
//  Produce C_PUSH ASM CodeBlock
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 888
//  Produce C_PUSH ASM CodeBlock
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command pop static 8
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@StaticTest.8
M=D
// For VM Command pop static 3
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@StaticTest.3
M=D
// For VM Command pop static 1
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@StaticTest.1
M=D
// For VM Command push static 3
//  Produce C_PUSH ASM CodeBlock
@StaticTest.3
D=M
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push static 1
//  Produce C_PUSH ASM CodeBlock
@StaticTest.1
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
// For VM Command push static 8
//  Produce C_PUSH ASM CodeBlock
@StaticTest.8
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
