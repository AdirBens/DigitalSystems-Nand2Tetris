import java.io.*;

/**
 * HackAssembler is an assembler that translates programs written in Hack assembly
 * language into the binary code understood by the Hack hardware platform
 */
public class HackAssembler {
    private final File asm;
    private final BufferedWriter HackWriter;

    private final Code encoder;
    private final SymbolTable symbolTable;

    private int ROMAddress;
    private int RAMAddress;

    /**
     * HackAssembler is an assembler object holds the responsibility of orchestrating the assembling process
     * @param asmFile Hack Assembly program file
     * @throws IOException if reading the given file is failed
     */
    public HackAssembler(File asmFile) throws IOException {
        if (asmFile.exists() && (asmFile.getName().endsWith(".asm"))){
            asm = asmFile;
        } else throw new IllegalArgumentException("[-] HackAssembler: expect HackAssembly program file with .asm extension.");

        String hackFileP = asmFile.getAbsolutePath().substring(0, asmFile.getAbsolutePath().indexOf(".asm")) + ".hack";
        File hackFile = new File(hackFileP);
        HackWriter = new BufferedWriter(new FileWriter(hackFile));

        encoder = new Code();
        symbolTable = new SymbolTable();
        RAMAddress = symbolTable.preDefSymbols;
        ROMAddress = 0;
    }

    /**
     * USAGE: > java HackAssembler <path to Prog.asm>.
     * @param args path to Prog.asm file as a command line argument
     * @throws IOException if reading the given file is failed
     */
    public static void main(String[] args) throws IOException {
        if (args.length != 1){
            throw new IllegalArgumentException("[-] HackAssembler USAGE: HackAssembler <path to Prog.asm>");
        }
        File asmFile = new File(args[0]);
        HackAssembler hackAssembler = new HackAssembler(asmFile);
        hackAssembler.assemble();
    }

    /**
     * Run an entire assembling process - starts with preRun process which collects symbols without produce code,
     * and after that, run full assembling sweep and translate HackAssembly commands into Hack-MachineLanguage binary code.
     * @throws IOException if reading the given file is failed
     */
    private void assemble() throws IOException {
        log("preforms pre assemble process");
        int symbolsDetected = preRun();
        log(symbolsDetected + " symbols were detected");
        log("is now assembling...");
        int commandsAssembled = Run();
        log(commandsAssembled + " commands assembled successfully.");
        close();
    }

    /**
     * Go through the entire assembly program, line by line, and build the `SymbolTable`.
     * Each time a pseudo-command (Xxx) is encountered, add a new entry to the symbol table,
     * associating Xxx with the ROM address that will eventually store the next command in the program.
     * @return number of symbols were add to SymbolTable
     */
    private int preRun() throws FileNotFoundException {
        int symbolsDetected = 0;
        Parser parser = new Parser(asm);

        while (parser.hasMoreCommands()) {
            parser.advance();
            switch (parser.currentCommandType){
                case COMMENT: continue;
                case EMPTY:   continue;
                case L_COMMAND:
                    {
                        symbolTable.addEntry(parser.symbol(), ROMAddress);
                        symbolsDetected++;
                    } break;
                case C_COMMAND:  ROMAddress++;
                    break;
                case  A_COMMAND: ROMAddress++;
                    break;
                default: break;
            }
        }
        parser.close();
        return symbolsDetected;
    }

    /**
     * Go through the entire assembly program, and parse it line by line.
     * translate each AssemblyCommands (line of code) into their binary Hack-Machine-Language representation,
     * and write it into `Prog.hack` machine language file.
     * @return number of 16bits binary Hack-Language commands written to file.
     */
    private int Run() throws IOException {
        int commandsAssembled = 0;
        Parser parser = new Parser(asm);

        while (parser.hasMoreCommands()){
            parser.advance();
            String command;

            switch (parser.currentCommandType){
                case A_COMMAND:
                    {   // Checks if A is symbolic or numeric address
                        command = parser.symbol();
                        int cNum = toNumber(command);
                        if (cNum != -1){  // which means A is a numeric address
                            command = String.format("%16s", Integer.toBinaryString(cNum)).replace(' ', '0');
                        } else {          // A is symbolic
                            if (!symbolTable.contains(command)) symbolTable.addEntry(command, RAMAddress++);
                            command = symbolTable.getBinaryAddress(command);
                        }
                    } break;
                case C_COMMAND:
                    {
                        String prefix = "111";
                        command = prefix + encoder.comp(parser.comp()) + encoder.dest(parser.dest()) + encoder.jump(parser.jump());
                    } break;
                default: continue;
            }

            writeLine(command);
            commandsAssembled++;
        }
        return commandsAssembled;
    }

    /**
     * Write to file and add newline after it.
     * @param line a line of Hack assembly code
     * @throws IOException if writing to file is failed
     */
    private void writeLine(String line) throws IOException {
        HackWriter.write(line);
        HackWriter.newLine();
    }

    /**
     * Parse a given string to its decimal value if possible.
     * @param s string to be converts
     * @return s decimal value if s contains only digits, else return -1
     */
    private int toNumber(String s){
        try { return Integer.parseInt(s); }
        catch (NumberFormatException e){ return -1; }
    }

    /**
     * release HackAssembler resources - output file stream
     */
    private void close() throws IOException {
        HackWriter.close();
    }

    /**
     * prints log message to stdout.
     * @param message a message to prompt to stdout
     */
    private void log(String message){
        System.out.println("[+] HackAssembler: " + message);
    }
}
