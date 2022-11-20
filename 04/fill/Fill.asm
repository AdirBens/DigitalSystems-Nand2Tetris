// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

(SETINGS) // Sets i to hold the address of end of screen
    @SCREEN
    D=A
    @8192
    D=D+A
    @i
    M=D
(KBD-LOOP)  // Check for user input
    @i
    D=M
    @SCREEN
    D=D-M
    @SETINGS
    D;JLE

    @KBD
    D=M
    @SET-BLACK
    D;JGT
    @SET-WHITE
    D;JEQ

(SET-BLACK)
    @i
    A=M
    M=-1
    @i
    M=M-1
    @KBD-LOOP
    0;JMP

(SET-WHITE)
    @i
    A=M
    M=0
    @i
    M=M-1
    @KBD-LOOP
    0;JMP

// (*) idle logic?