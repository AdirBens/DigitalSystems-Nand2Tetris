
// ------------------------Mon Dec 26 22:42:09 2022------------------------
// VMTranslator - Translation Of StackTest.vm to HackAssembly code.
//  [+] Translation end successfully.
//      [>] 38 VM Code lines parsed
//      [>] 430 ASM Code lines produced.
//      [>] Translation ratio is 11.31578947368421
// ------------------------------------------------------------------------

// For VM Command push constant 17
//  Produce C_PUSH ASM CodeBlock
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 17
//  Produce C_PUSH ASM CodeBlock
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command eq
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE1
D;JNE
@TRUE1
D;JEQ
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
// For VM Command push constant 17
//  Produce C_PUSH ASM CodeBlock
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 16
//  Produce C_PUSH ASM CodeBlock
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command eq
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE2
D;JNE
@TRUE2
D;JEQ
(TRUE2)
@SP
A=M
M=-1
@CONTINUE2
D;JMP
(FALSE2)
@SP
A=M
M=0
@CONTINUE2
D;JMP
(CONTINUE2)
@SP
M=M+1
// For VM Command push constant 16
//  Produce C_PUSH ASM CodeBlock
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 17
//  Produce C_PUSH ASM CodeBlock
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command eq
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE3
D;JNE
@TRUE3
D;JEQ
(TRUE3)
@SP
A=M
M=-1
@CONTINUE3
D;JMP
(FALSE3)
@SP
A=M
M=0
@CONTINUE3
D;JMP
(CONTINUE3)
@SP
M=M+1
// For VM Command push constant 892
//  Produce C_PUSH ASM CodeBlock
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 891
//  Produce C_PUSH ASM CodeBlock
@891
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
@FALSE4
D;JGE
@TRUE4
D;JLT
(TRUE4)
@SP
A=M
M=-1
@CONTINUE4
D;JMP
(FALSE4)
@SP
A=M
M=0
@CONTINUE4
D;JMP
(CONTINUE4)
@SP
M=M+1
// For VM Command push constant 891
//  Produce C_PUSH ASM CodeBlock
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 892
//  Produce C_PUSH ASM CodeBlock
@892
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
@FALSE5
D;JGE
@TRUE5
D;JLT
(TRUE5)
@SP
A=M
M=-1
@CONTINUE5
D;JMP
(FALSE5)
@SP
A=M
M=0
@CONTINUE5
D;JMP
(CONTINUE5)
@SP
M=M+1
// For VM Command push constant 891
//  Produce C_PUSH ASM CodeBlock
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 891
//  Produce C_PUSH ASM CodeBlock
@891
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
@FALSE6
D;JGE
@TRUE6
D;JLT
(TRUE6)
@SP
A=M
M=-1
@CONTINUE6
D;JMP
(FALSE6)
@SP
A=M
M=0
@CONTINUE6
D;JMP
(CONTINUE6)
@SP
M=M+1
// For VM Command push constant 32767
//  Produce C_PUSH ASM CodeBlock
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 32766
//  Produce C_PUSH ASM CodeBlock
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command gt
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE7
D;JLE
@TRUE7
D;JGT
(TRUE7)
@SP
A=M
M=-1
@CONTINUE7
D;JMP
(FALSE7)
@SP
A=M
M=0
@CONTINUE7
D;JMP
(CONTINUE7)
@SP
M=M+1
// For VM Command push constant 32766
//  Produce C_PUSH ASM CodeBlock
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 32767
//  Produce C_PUSH ASM CodeBlock
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command gt
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE8
D;JLE
@TRUE8
D;JGT
(TRUE8)
@SP
A=M
M=-1
@CONTINUE8
D;JMP
(FALSE8)
@SP
A=M
M=0
@CONTINUE8
D;JMP
(CONTINUE8)
@SP
M=M+1
// For VM Command push constant 32766
//  Produce C_PUSH ASM CodeBlock
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 32766
//  Produce C_PUSH ASM CodeBlock
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command gt
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@FALSE9
D;JLE
@TRUE9
D;JGT
(TRUE9)
@SP
A=M
M=-1
@CONTINUE9
D;JMP
(FALSE9)
@SP
A=M
M=0
@CONTINUE9
D;JMP
(CONTINUE9)
@SP
M=M+1
// For VM Command push constant 57
//  Produce C_PUSH ASM CodeBlock
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 31
//  Produce C_PUSH ASM CodeBlock
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command push constant 53
//  Produce C_PUSH ASM CodeBlock
@53
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
// For VM Command push constant 112
//  Produce C_PUSH ASM CodeBlock
@112
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
// For VM Command neg
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
M=-M
@SP
M=M+1
// For VM Command and
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M&D
@SP
M=M+1
// For VM Command push constant 82
//  Produce C_PUSH ASM CodeBlock
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// For VM Command or
//  Produce C_ARITHMETIC ASM CodeBlock
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M|D
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
