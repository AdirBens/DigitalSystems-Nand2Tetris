import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.*;
import java.nio.file.InvalidPathException;
import java.util.Iterator;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.stream.Stream;

/**
 * Reads an assembly language command, parses it, and provides convenient access to the command’s components
 * (fields and symbols). In addition, removes all white space and comments.
 */
public class Parser {
    private final Iterator<String> tokens;
    private String currentCommand;
    private Scanner fileScanner;

    private enum CommandType {
        A_COMMAND(Pattern.compile("^@")),
        C_COMMAND(Pattern.compile("((^\\p{Alnum}+=(\\p{Alnum}&&[^;])$+)|((^\\p{Alnum}&&[^=])+;(\\p{Alnum}&&[^=])+$))")),
        L_COMMAND(Pattern.compile("^\\(\\p{Alnum}+\\)$"));
        private Pattern commandPattern;
        private CommandType(Pattern commandPattern){
            this.commandPattern = commandPattern;
        }
    }

    public Parser(File file) throws FileNotFoundException, InvalidPathException {
        FileNameExtensionFilter extensionFilter = new FileNameExtensionFilter(null, "asm");
        if (!file.exists()){
            throw new FileNotFoundException(file.getAbsolutePath());
        } else if (!extensionFilter.accept(file)){
            throw new InvalidPathException(file.getPath(),
                    "The Hack assembler expects text file with .asm extension, contains a Hack assembly program");
        } else {
            fileScanner = new Scanner(file);
            tokens = fileTokenizer(fileScanner);
        }
    }

    /**
     * @return true if the iteration has more elements.
     */
    public boolean hasMoreCommands(){
        return tokens.hasNext();
    }

    /**
     * Reads the next command from the input and makes it the current command.
     * Should be called only if hasMoreCommands() is true. Initially there is no current command.
     */
    public void advance(){
        if (hasMoreCommands()) currentCommand = tokens.next();
    }

    /**
     * Returns the type of the current command:
     * @return A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
     *         C_COMMAND for dest=comp;jump
     *         L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.
     */
    public CommandType commandType(){
        for (CommandType c: CommandType.values()){
            if (c.commandPattern.matcher(currentCommand).find()) return c;
        }
        return null;
    }

    /**
     * Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
     * Should be called only when commandType() is A_COMMAND or L_COMMAND.
     * @return
     */
    public String symbol(){
        String symbol;
        switch (commandType()){
            case A_COMMAND : symbol = currentCommand.substring(1);
                break;
            case L_COMMAND : symbol = currentCommand.substring(1, currentCommand.length() - 2);
                break;
            default: symbol = "";
                break;
        }
        return symbol;
    }

    /**
     * Returns the dest mnemonic in the current C-command (8 possibilities).
     * Should be called only when commandType() is C_COMMAND.
     * @return
     */
    public String dest(){
        String dest;
        switch (commandType()){
            case C_COMMAND : dest = currentCommand.substring(0, currentCommand.indexOf("="));
                break;
            default: dest = "";
        }
        return dest;
    }

    /**
     * Returns the comp mnemonic in the current C-command (28 possibilities).
     * Should be called only when commandType() is C_COMMAND.
     * @return
     */
    public String comp() {
        String comp;
        switch (commandType()) {
            // TODO: consider to user comp length (num of bits) instead indexof;
            case C_COMMAND:
                comp = currentCommand.substring(currentCommand.indexOf("=") + 1,
                        currentCommand.indexOf(";") - 1);
                break;
            default:
                comp = "";
        }
        return comp;
    }
    /**
     * Returns the jump mnemonic in the current C-command (8 possibilities).
     * Should be called only when commandType() is C_COMMAND.
     * @return
     */
    public String jump(){
        String jump;
        switch (commandType()){
            // TODO: consider to user comp length (num of bits) instead indexof;
            case C_COMMAND : jump = currentCommand.substring(currentCommand.indexOf(";") - 1);
                break;
            default: jump = "";
        }
          return jump;
    }

    /**
     *
     * @param fileScanner
     * @return
     */
    private Iterator<String> fileTokenizer(Scanner fileScanner){
        Stream<String> filteredFile = fileScanner.tokens().filter((String line) ->{return !line.startsWith("//");});
        return filteredFile.iterator();
    }

    /**
     *
     */
    public void closeFile(){
        fileScanner.close();
    }
}
