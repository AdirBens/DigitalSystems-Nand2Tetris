
// ----------------------------  Wed Dec 28 22:45:54 2022  ----------------------------
// VMTranslation Session - Translation of vm files in StaticsTest to HackAssembly code.
// [>>]  Detected .vm files - Sys.vm, Class1.vm, Class2.vm
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  12 VM Code lines parsed.
//      [+] VMTranslator:  648 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 54.0 has been reached.
// ------------------------------------------------------------------------------------


// For VM Command init
//  Produce C_INIT ASM CodeBlock
@256
D=A
@SP
M=D

// For VM Command call Sys.init 0
//  Produce C_CALL ASM CodeBlock
@Sys.init_return_address1 // Push return-address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // Push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // Push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // Push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // Push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG=SP-n-5
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Sys.init //Goto function
0;JMP
(Sys.init_return_address1)

// For VM Command function Sys.init 0
//  Produce C_FUNCTION ASM CodeBlock
(Sys.init)

// For VM Command push constant 6
//  Produce C_PUSH ASM CodeBlock
@6
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

// For VM Command call Class1.set 2
//  Produce C_CALL ASM CodeBlock
@Class1.set_return_address2 // Push return-address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // Push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // Push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // Push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // Push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG=SP-n-5
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Class1.set //Goto function
0;JMP
(Class1.set_return_address2)

// For VM Command pop temp 0
//  Produce C_POP ASM CodeBlock
@5
D=A
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

// For VM Command push constant 23
//  Produce C_PUSH ASM CodeBlock
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push constant 15
//  Produce C_PUSH ASM CodeBlock
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command call Class2.set 2
//  Produce C_CALL ASM CodeBlock
@Class2.set_return_address3 // Push return-address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // Push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // Push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // Push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // Push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG=SP-n-5
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Class2.set //Goto function
0;JMP
(Class2.set_return_address3)

// For VM Command pop temp 0
//  Produce C_POP ASM CodeBlock
@5
D=A
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

// For VM Command call Class1.get 0
//  Produce C_CALL ASM CodeBlock
@Class1.get_return_address4 // Push return-address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // Push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // Push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // Push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // Push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG=SP-n-5
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Class1.get //Goto function
0;JMP
(Class1.get_return_address4)

// For VM Command call Class2.get 0
//  Produce C_CALL ASM CodeBlock
@Class2.get_return_address5 // Push return-address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // Push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // Push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // Push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // Push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG=SP-n-5
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Class2.get //Goto function
0;JMP
(Class2.get_return_address5)

// For VM Command label WHILE
//  Produce C_LABEL ASM CodeBlock
(Sys.init$WHILE)

// For VM Command goto WHILE
//  Produce C_GOTO ASM CodeBlock
@Sys.init$WHILE
0;JMP

// For VM Command function Class1.set 0
//  Produce C_FUNCTION ASM CodeBlock
(Class1.set)

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

// For VM Command pop static 0
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@Class1.0
M=D

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

// For VM Command pop static 1
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@Class1.1
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

// For VM Command function Class1.get 0
//  Produce C_FUNCTION ASM CodeBlock
(Class1.get)

// For VM Command push static 0
//  Produce C_PUSH ASM CodeBlock
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push static 1
//  Produce C_PUSH ASM CodeBlock
@Class1.1
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

// For VM Command function Class2.set 0
//  Produce C_FUNCTION ASM CodeBlock
(Class2.set)

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

// For VM Command pop static 0
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@Class2.0
M=D

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

// For VM Command pop static 1
//  Produce C_POP ASM CodeBlock
@SP
AM=M-1
D=M
@Class2.1
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

// For VM Command function Class2.get 0
//  Produce C_FUNCTION ASM CodeBlock
(Class2.get)

// For VM Command push static 0
//  Produce C_PUSH ASM CodeBlock
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push static 1
//  Produce C_PUSH ASM CodeBlock
@Class2.1
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
