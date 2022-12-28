
// ----------------------------  Wed Dec 28 22:45:14 2022  ----------------------------
// VMTranslation Session - Translation of SimpleFunction.vm to HackAssembly code.
// [>>]  Detected .vm files -  SimpleFunction.vm
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  10 VM Code lines parsed.
//      [+] VMTranslator:  140 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 14.0 has been reached.
// ------------------------------------------------------------------------------------


// For VM Command function SimpleFunction.test 2
//  Produce C_FUNCTION ASM CodeBlock
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1

@SP
A=M
M=0
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

// For VM Command push local 1
//  Produce C_PUSH ASM CodeBlock
@LCL
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

// For VM Command not
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
M=!M
@SP
M=M+1

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

// For VM Command return
//  Produce C_RETURN ASM CodeBlock
@LCL // FRAME=LCL
D=M
@FRAME
M=D
@5 // RET=*(FRAME-5)
D=D-A
A=D
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1 // SP=ARG+1
@SP
M=D
@FRAME // THAT=*(FRAME-1)
D=M-1
A=D
D=M
@THAT
M=D
@2 // THIS=*(FRAME-2)
D=A
@FRAME
D=M-D
A=D
D=M
@THIS
M=D
@3 // ARG=*(FRAME-3)
D=A
@FRAME
D=M-D
A=D
D=M
@ARG
M=D
@4 // LCL=*(FRAME-4)
D=A
@FRAME
D=M-D
A=D
D=M
@LCL
M=D
@RET
A=M
0;JMP
