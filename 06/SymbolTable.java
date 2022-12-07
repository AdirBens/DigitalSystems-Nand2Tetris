import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;


/**
 * Hack's SymbolTable
 * create and maintain the correspondence between symbols and their meaning.
 * particularly resolves Symbol into its actual Address in Hack's RAM and ROM spaces.
 */
public class SymbolTable {
    static Pattern validUserSymbol = Pattern.compile("^([[a-zA-Z]|[._$:]])([\\p{Alnum}|[._$:]])*$");
    private Map<String, Integer> symbols;

    public SymbolTable(){
        symbols = new HashMap<>();
        loadPreDefinedSymbols();
    }

    /**
     * Adds the pair <symbol, address> to the table.
     * A user-defined symbol can be any sequence of letters, digits, underscore (_),
     * dot (.), dollar sign ($), and colon (:) that does not begin with a digit.
     * @param symbol
     * @param address
     */
    public void addEntry(String symbol, int address){
        if (validUserSymbol.matcher(symbol).find()){
            symbols.put(symbol, address);
        } else throw new IllegalArgumentException("[-] HackAssembler: " + symbol + " is illegal.\n" +
                "A user-defined symbol is a sequence of letters, digits, underscore(_), dot(.), dollar-sign ($) " +
                "and colon(:) that does not begin with digit");
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
     * return the RAM address which symbol is mapped to in decimal form
     * @param symbol
     * @return decimal RAM address if symbol exists in table, else -1
     */
    public int getDecimalAddress(String symbol){
        if (contains(symbol)){
            return symbols.get(symbol);
        } else return -1;
    }

    /**
     * return the RAM address which symbol is mapped to in Binary form
     * @param symbol
     * @return 16Bits Binary RAM address if symbol exists in table, else ""
     */
    public String getBinaryAddress(String symbol){
        int dec = getDecimalAddress(symbol);
        if (dec != -1){
            return String.format("%16s", Integer.toBinaryString(dec)).replace(' ', '0');
        } else return "";
    }

    /**
     * Any Hack assembly program is allowed to use the following predefined symbols.
     *  (!) Note that each one of the top five RAM locations can be referred to using two predefined symbols.
     *      For example, either R2 or ARG can be used to refer to RAM[2].
     */
    private void loadPreDefinedSymbols(){
        symbols.put("SP", 0);
        symbols.put("LCL", 1);
        symbols.put("ARG", 2);
        symbols.put("THIS", 3);
        symbols.put("THAT", 4);
        symbols.put("SCREEN", 16384);
        symbols.put("KBD", 24576);

        for (int i = 0; i < 16; i++) symbols.put("R"+i, i);
    }
}
