
// ----------------------------  Wed Dec 28 22:28:07 2022  ----------------------------
// VMTranslation Session - Translation of vm files in FibonacciElement to HackAssembly code.
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  20 VM Code lines parsed.
//      [+] VMTranslator:  445 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 22.25 has been reached.
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

// For VM Command push constant 4
//  Produce C_PUSH ASM CodeBlock
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command call Main.fibonacci 1
//  Produce C_CALL ASM CodeBlock
@Main.fibonacci_return_address2 // Push return-address
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Main.fibonacci //Goto function
0;JMP
(Main.fibonacci_return_address2)

// For VM Command label WHILE
//  Produce C_LABEL ASM CodeBlock
(Sys.init$WHILE)

// For VM Command goto WHILE
//  Produce C_GOTO ASM CodeBlock
@Sys.init$WHILE
0;JMP

// For VM Command function Main.fibonacci 0
//  Produce C_FUNCTION ASM CodeBlock
(Main.fibonacci)

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

// For VM Command lt
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE1
D;JGE
@TRUE1
D;JLT
(TRUE1)
@SP
A=M
M=-1
@CONTINUE1
D;JMP
(FALSE1)
@SP
A=M
M=0
@CONTINUE1
D;JMP
(CONTINUE1)
@SP
M=M+1

// For VM Command if-goto IF_TRUE
//  Produce C_IF ASM CodeBlock
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE

// For VM Command goto IF_FALSE
//  Produce C_GOTO ASM CodeBlock
@Main.fibonacci$IF_FALSE
0;JMP

// For VM Command label IF_TRUE
//  Produce C_LABEL ASM CodeBlock
(Main.fibonacci$IF_TRUE)

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

// For VM Command label IF_FALSE
//  Produce C_LABEL ASM CodeBlock
(Main.fibonacci$IF_FALSE)

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

// For VM Command call Main.fibonacci 1
//  Produce C_CALL ASM CodeBlock
@Main.fibonacci_return_address3 // Push return-address
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Main.fibonacci //Goto function
0;JMP
(Main.fibonacci_return_address3)

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

// For VM Command call Main.fibonacci 1
//  Produce C_CALL ASM CodeBlock
@Main.fibonacci_return_address4 // Push return-address
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
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP // LCL=SP
D=M
@LCL
M=D
@Main.fibonacci //Goto function
0;JMP
(Main.fibonacci_return_address4)

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
