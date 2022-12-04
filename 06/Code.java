import java.util.HashMap;
import java.util.Map;

public class Code {
    private final Map<String, String> compTable;
    private final Map<String, String> destTable;
    private final Map<String, String> jumpTable;

    public Code(){
        this.compTable = new HashMap<>();
        buildCompTable();
        this.destTable = new HashMap<>();
        buildDestTable();
        this.jumpTable = new HashMap<>();
        buildJumpTable();
    }

    /**
     * @param mne - Hack assembly language mnemonic
     * @return the binary code of the `dest` mnemonic (3 bits as String)
     */
    public String dest(String mne){
        return destTable.get(mne);
    }

    /**
     * @param mne - Hack assembly language mnemonic
     * @return the binary code of the `comp` mnemonic (3 bits as String)
     */
    public String comp(String mne){
        return compTable.get(mne);
    }

    /**
     * @param mne - Hack assembly language mnemonic
     * @return the binary code of the `jump` mnemonic (3 bits as String)
     */
    public String jump(String mne){
        return jumpTable.get(mne);
    }

    private void buildCompTable(){
        compTable.put("0", "101010");
        compTable.put("1", "111111");
        compTable.put("-1", "111010");
        compTable.put("D", "001100");
        compTable.put("A", "110000");
        compTable.put("M", "110000");
        compTable.put("!D", "001101");
        compTable.put("!A", "110001");
        compTable.put("!M", "110001");
        compTable.put("-D", "001111");
        compTable.put("-A", "110011");
        compTable.put("-M", "110011");
        compTable.put("D+1", "011111");
        compTable.put("A+1", "110111");
        compTable.put("M+1", "110111");
        compTable.put("D-1", "001110");
        compTable.put("A-1", "110010");
        compTable.put("M-1", "110010");
        compTable.put("D+A", "110010");
        compTable.put("D+M", "110010");
        compTable.put("D-A", "010011");
        compTable.put("D-M", "010011");
        compTable.put("A-D", "000111");
        compTable.put("M-D", "000111");
        compTable.put("D&A", "000000");
        compTable.put("D&M", "000000");
        compTable.put("D|A", "010101");
        compTable.put("D|M", "010101");
    }

    private void buildDestTable(){
        destTable.put("null", "000");
        destTable.put("M", "001");
        destTable.put("D", "010");
        destTable.put("MD", "011");
        destTable.put("A", "100");
        destTable.put("AM", "101");
        destTable.put("AD", "110");
        destTable.put("AMD", "111");
    }

    private void buildJumpTable(){
        jumpTable.put("null", "000");
        jumpTable.put("JGT", "001");
        jumpTable.put("JEQ", "010");
        jumpTable.put("JGE", "100");
        jumpTable.put("JLT", "101");
        jumpTable.put("JLE", "110");
        jumpTable.put("JMP", "111");
    }
}
