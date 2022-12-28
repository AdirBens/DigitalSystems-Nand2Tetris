
// ----------------------------  Wed Dec 28 22:35:44 2022  ----------------------------
// VMTranslation Session - Translation of vm files in NestedCall to HackAssembly code.
//   [>] VMTranslator:  Translation end successfully.
//      [+] VMTranslator:  42 VM Code lines parsed.
//      [+] VMTranslator:  569 Assembly Code lines produced.
//      [+] VMTranslator:  Translation ration 13.547619047619047 has been reached.
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

// For VM Command push constant 4000
//  Produce C_PUSH ASM CodeBlock
@4000
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

// For VM Command push constant 5000
//  Produce C_PUSH ASM CodeBlock
@5000
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

// For VM Command call Sys.main 0
//  Produce C_CALL ASM CodeBlock
@Sys.main_return_address2 // Push return-address
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
@Sys.main //Goto function
0;JMP
(Sys.main_return_address2)

// For VM Command pop temp 1
//  Produce C_POP ASM CodeBlock
@5
D=A
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

// For VM Command label LOOP
//  Produce C_LABEL ASM CodeBlock
(Sys.init$LOOP)

// For VM Command goto LOOP
//  Produce C_GOTO ASM CodeBlock
@Sys.init$LOOP
0;JMP

// For VM Command function Sys.main 5
//  Produce C_FUNCTION ASM CodeBlock
(Sys.main)
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

@SP
A=M
M=0
@SP
M=M+1


// For VM Command push constant 4001
//  Produce C_PUSH ASM CodeBlock
@4001
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

// For VM Command push constant 5001
//  Produce C_PUSH ASM CodeBlock
@5001
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

// For VM Command push constant 200
//  Produce C_PUSH ASM CodeBlock
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop local 1
//  Produce C_POP ASM CodeBlock
@LCL
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

// For VM Command push constant 40
//  Produce C_PUSH ASM CodeBlock
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop local 2
//  Produce C_POP ASM CodeBlock
@LCL
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

// For VM Command push constant 6
//  Produce C_PUSH ASM CodeBlock
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command pop local 3
//  Produce C_POP ASM CodeBlock
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// For VM Command push constant 123
//  Produce C_PUSH ASM CodeBlock
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// For VM Command call Sys.add12 1
//  Produce C_CALL ASM CodeBlock
@Sys.add12_return_address3 // Push return-address
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
@Sys.add12 //Goto function
0;JMP
(Sys.add12_return_address3)

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

// For VM Command push local 2
//  Produce C_PUSH ASM CodeBlock
@LCL
D=M
@2
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push local 3
//  Produce C_PUSH ASM CodeBlock
@LCL
D=M
@3
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// For VM Command push local 4
//  Produce C_PUSH ASM CodeBlock
@LCL
D=M
@4
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

// For VM Command function Sys.add12 0
//  Produce C_FUNCTION ASM CodeBlock
(Sys.add12)

// For VM Command push constant 4002
//  Produce C_PUSH ASM CodeBlock
@4002
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

// For VM Command push constant 5002
//  Produce C_PUSH ASM CodeBlock
@5002
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

// For VM Command push constant 12
//  Produce C_PUSH ASM CodeBlock
@12
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
