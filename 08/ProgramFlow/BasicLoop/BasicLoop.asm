
// -------------------------- Wed Dec 28 22:19:39 2022 --------------------------
// VMTranslation Session - Translation of BasicLoop.asm to HackAssembly code.
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  14 VM Code lines parsed.
//      [+] VMTranslator:  127 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 9.071428571428571 has been reached.
// ------------------------------------------------------------------------------


// For VM Command push constant 0
//  Produce C_PUSH ASM CodeBlock
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop local 0
//  Produce C_POP ASM CodeBlock
@LCL
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

// For VM Command label LOOP_START
//  Produce C_LABEL ASM CodeBlock
(LOOP_START)

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

// For VM Command push local 0
//  Produce C_PUSH ASM CodeBlock
@LCL
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

// For VM Command pop local 0
//  Produce C_POP ASM CodeBlock
@LCL
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

// For VM Command if-goto LOOP_START
//  Produce C_IF ASM CodeBlock
@SP
AM=M-1
D=M
@LOOP_START
D;JNE

// For VM Command push local 0
//  Produce C_PUSH ASM CodeBlock
@LCL
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
