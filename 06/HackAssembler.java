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

    public HackAssembler(File asmFile) throws IOException {
        if (asmFile.exists() && (asmFile.getName().endsWith(".asm"))){
            asm = asmFile;
        } else throw new IllegalArgumentException("[-] HackAssembler: expect HackAssembly program file with .asm extension.");

        String hackFileP = asmFile.getAbsolutePath().substring(0, asmFile.getAbsolutePath().indexOf(".asm")) + ".hack";
        File hackFile = new File(hackFileP);
        HackWriter = new BufferedWriter(new FileWriter(hackFile));

        encoder = new Code();
        symbolTable = new SymbolTable();
        RAMAddress = 16;
        ROMAddress = 0;
    }

    /**
     * USAGE: > java HackAssembler <path to Prog.asm>.
     * @param args
     * @throws IOException
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
     * @throws IOException
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

        while (parser.hasMoreCommands()){
            parser.advance();
            parser.commandType();
            if (parser.currentCommandType == Command.L_COMMAND) {
                symbolTable.addEntry(parser.symbol(), ROMAddress);
                symbolsDetected++;
            } else if (parser.currentCommandType == Command.A_COMMAND || parser.currentCommandType == Command.C_COMMAND) {
                ROMAddress++;
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
            parser.commandType();

            String command;
            if (parser.currentCommandType == Command.A_COMMAND){
                command = parser.symbol();
                int cNum = toNumber(command);
                if (cNum != -1){ // A is a numeric address
                    command = String.format("%16s", Integer.toBinaryString(cNum)).replace(' ', '0');
                } else {          // A is symbolic
                    if (!symbolTable.contains(command)) symbolTable.addEntry(command, RAMAddress++);
                    command = symbolTable.getBinaryAddress(command);
                }
            } else if (parser.currentCommandType == Command.C_COMMAND) {
                command = "111" + encoder.comp(parser.comp()) + encoder.dest(parser.dest()) + encoder.jump(parser.jump());
            } else continue;

            writeLine(command);
            commandsAssembled++;
        }
        return commandsAssembled;
    }

    /**
     * Write to file and add newline after it.
     * @param line
     * @throws IOException
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
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e){
            return -1;
        }
    }

    /**
     * release HackAssembler resources - output file stream
     */
    private void close() throws IOException {
        HackWriter.close();
    }

    /**
     * prints log message to stdout.
     * @param message
     */
    private void log(String message){
        System.out.println("[+] HackAssembler: " + message);
    }
}
