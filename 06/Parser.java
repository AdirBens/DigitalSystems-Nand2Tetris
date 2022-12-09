import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Hack Parser -
 * parse a given Prog.asm Hack Assembly program file, into HackCommand.
 * for each command found, holds its type and relevant fields according to command type.
 */
public class Parser {
    private final Scanner asmC;
    private String currentCommand;
    public Command currentCommandType;

    /**
     * @param asmProgFile Prog.asm HackAssembly program.
     * @throws FileNotFoundException
     */
    public Parser(File asmProgFile) throws FileNotFoundException {
        asmC = new Scanner(asmProgFile);
    }

    /**
     * Checks if there are more commands available
     * @return true if there is next command to parse, false else.
     */
    public boolean hasMoreCommands(){
        return asmC.hasNextLine();
    }

    /**
     * set parser's current command to be the next command from file iterator (scanner).
     */
    public void advance(){
        if (hasMoreCommands()){
            currentCommand = asmC.nextLine();
            currentCommand = removeInLineComments(currentCommand);
            currentCommandType = commandType();
        }
    }

    /**
     * Determine parser's current command's type.
     * @return Returns the type of the current command (a member of Command enum):
     *         (-) A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number.
     *         (-) C_COMMAND for dest=comp;jump.
     *         (-) L_COMMAND (which it pseudo-command) for (Xxx) where Xxx is a symbol.
     *         if current command does not fit any member of Command enum, returns null;
     */
    public Command commandType(){
        for (Command c: Command.values()){
            if (c.pattern.matcher(currentCommand).find()){
                currentCommandType = c;
                return c;
            }
        }
        return null;
    }

    /**
     * @return Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
     * Should be called only when commandType() is A_COMMAND or L_COMMAND, else return "null"
     */
    public String symbol(){
        String symbol = "null";
        if ((currentCommandType == Command.L_COMMAND) || (currentCommandType == Command.A_COMMAND)){
            Matcher m = currentCommandType.pattern.matcher(currentCommand);
            symbol = (m.find())? m.group(1) : "null";
        }
        symbol = (symbol == null)? "null" : symbol;
        return symbol;
    }

    /**
     * @return Returns the dest mnemonic in the current C_COMMAND (8 possibilities).
     * Should be called only when commandType() is C_COMMAND, else return "null".
     */
    public String dest(){
        String dest = "null";
        if ((currentCommandType == Command.C_COMMAND)){
            Matcher m = currentCommandType.pattern.matcher(currentCommand);
            dest = (m.find())? m.group(2) : "null";
        }
        dest = (dest == null)? "null" : dest;
        return dest;
    }

    /**
     * @return Returns the comp mnemonic in the current C_COMMAND (28 possibilities).
     * Should be called only when commandType() is C_COMMAND, else return "null".
     */
    public String comp(){
        String comp = "null";
        if ((currentCommandType == Command.C_COMMAND)){
            Matcher m = currentCommandType.pattern.matcher(currentCommand);
            comp = (m.find())? m.group(3) : "null";
        }
        comp = (comp == null)? "null" : comp;
        return comp;
    }

    /**
     * @return Returns the jump mnemonic in the current C_COMMAND (8 possibilities).
     * Should be called only when commandType() is C_COMMAND, else return "null".
     */
    public String jump(){
        String jump = "null";
        if ((currentCommandType == Command.C_COMMAND)){
            Matcher m = currentCommandType.pattern.matcher(currentCommand);
            jump = (m.find())? m.group(5) : "null";
        }
        jump = (jump == null)? "null" : jump;
        return jump;
    }

    /**
     * Release Parser's resources - closes Scanner file input stream.
     */
    public void close(){
        asmC.close();
    }

    /**
     * @param line
     * @return The given line stripped from in-line comments.
     */
    private String removeInLineComments(String line){
        Pattern inlineCommentP = Pattern.compile("(^.*)//.*$");
        Matcher commentMatcher = inlineCommentP.matcher(line);
        if (commentMatcher.find()){
            line = commentMatcher.group(1);
        }
        return line.strip();
    }
}
