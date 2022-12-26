
// ------------------------Mon Dec 26 22:41:58 2022------------------------
// VMTranslator - Translation Of SimpleAdd.vm to HackAssembly code.
//  [+] Translation end successfully.
//      [>] 3 VM Code lines parsed
//      [>] 22 ASM Code lines produced.
//      [>] Translation ratio is 7.333333333333333
// ------------------------------------------------------------------------

// For VM Command push constant 7
//  Produce C_PUSH ASM CodeBlock
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 8
//  Produce C_PUSH ASM CodeBlock
@8
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
