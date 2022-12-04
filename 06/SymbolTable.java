import java.security.InvalidKeyException;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class SymbolTable {
    protected Map<String, Integer> symbols;
    protected Pattern validSymbolPattern;

    public SymbolTable() throws PatternSyntaxException {
        // TODO: consider variable-symbols, label-symbols, predefine-symbols and user-defined symbols
        this.symbols = new HashMap<>();
        loadPreDefineSymbols();
        this.validSymbolPattern = Pattern.compile("^(\\p{Alpha}|\\$|\\.|:|_)+(\\p{Alnum}|\\$|\\.|:|_)*");
    }

    /**
     * Adds the pair <symbol, address> to the table.
     * A user-defined symbol can be any sequence of letters, digits, underscore (_),
     * dot (.), dollar sign ($), and colon (:) that does not begin with a digit.
     * @param symbol
     * @param address
     */
    public void addEntry(String symbol, int address) throws InvalidKeyException {
        Matcher matcher = validSymbolPattern.matcher(symbol);
        if (matcher.find()) {
            symbols.put(symbol, address);
        } else {
            throw new InvalidKeyException("Invalid symbol: A user-defined symbol can be any sequence of letters/" +
                    ", digits, underscore, dot, dollar sign, and colon, that does not begin with a digit");
        }
    }

    /**
     * Check weather the table contains the given symbol
     * @param symbol
     * @return
     */
    public boolean contains(String symbol){
        return symbols.containsKey(symbol);
    }

    /**
     * Returns the address associated with the symbol
     * @param symbol
     * @return the address of given symbol or null if table contains no mapping for the symbol
     */
    public int GetAddress(String symbol){
        return symbols.get(symbol);
    }

    /**
     * Any Hack assembly program is allowed to use the following predefined symbols.
     *  Note that each one of the top five RAM locations can be referred to using two predefined symbols.
     *  For example, either R2 or ARG can be used to refer to RAM[2].
     */
    private void loadPreDefineSymbols(){
        symbols.put("SP", 0);
        symbols.put("LCL", 1);
        symbols.put("ARG", 2);
        symbols.put("THIS", 3);
        symbols.put("THAT", 4);
        symbols.put("R0", 0);
        symbols.put("R1", 1);
        symbols.put("R2", 2);
        symbols.put("R3", 3);
        symbols.put("R4", 4);
        symbols.put("R5", 5);
        symbols.put("R6", 6);
        symbols.put("R7", 7);
        symbols.put("R8", 8);
        symbols.put("R9", 9);
        symbols.put("R10", 10);
        symbols.put("R11", 11);
        symbols.put("R12", 12);
        symbols.put("R13", 13);
        symbols.put("R14", 14);
        symbols.put("R15", 15);
        symbols.put("SCREEN", 16384);
        symbols.put("KBD", 24576);
    }
}
