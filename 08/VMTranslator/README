# VMTranslator - Translates JackVM Programs to HackAssembly program
### Adir Ben-Shimol & Yehuda Band


## Pre-Requisite:
1. Python version >= 3.8
    - os, argparse, time libraries must be available.

## Usage:
open terminal (cmd, powershell, bash, etc..)
`{ python <VMTranslator.py> <Prog.vm> }`
where <xxx> is path to corresponding file.

as a results for the above command, VMTranslator creates
Prog.asm file in at the same directory as given Prog.vm file.
This Prog.asm file contains a HackAssembly commands with equivalent functionality as the JackVM program in Prog.vm file.


## Technical:
VMTranslator contains 5 modules, each play role in the translation process, provides together more scalable an modular VMTranslator.
- VMTranslator - The main module who orchestrate the process of translate Jack-VMFiles into corresponding Hack Assembly code.
- Parser - Parse Commands from a Jack-VMFile, and encapsulates access to the input code. yields a Command Object for each parsed command.
- CodeWriter - Translate JackVM Commands into HackAssembly Code according to Machine's Standard-Mapping.
- Command - Command object stands for extracting command's components from VMCommand string, and providing convenient and safe access to components.
- MachineLanguage - Holds MachineLanguage Assembly common Routines and base Templates.

(!) Notice that we provide you the ability to choose if the produces .asm file include header with info about translation process,
    and the ratio between number of VM command verses Assembly commands.
    at module `VMTranslator._log_file(), pass the argument `header=True` to append header data to produce file - this cuse to read the whole file and write it again.
