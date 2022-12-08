import java.util.HashMap;
import java.util.Map;


/**
 * Translates Hack assembly language C-Instructions mnemonics into binary codes.
 *  C-Instruction : dest=comp;jump
 */
public class Code {
    Map<String, String> compTable;
    Map<String, String> destTable;
    Map<String, String> jumpTable;

    /**
     * Construct new Code object which can use as HackAssembly encoder
     *  loads Hack's assembly mnemonics tables (comp, dest, jump)
     */
    public Code(){
        buildCompTable();
        buildDestTable();
        buildJumpTable();
    }

    /**
     * @param mne Hack assembly language mnemonic
     * @return the binary code of the `comp` mnemonic (3 bits as String)
     */
    public String comp(String mne){
        return compTable.get(mne);
    }

    /**
     * @param mne Hack assembly language mnemonic
     * @return the binary code of the `dest` mnemonic (3 bits as String)
     */
    public String dest(String mne){
        return destTable.get(mne);
    }

    /**
     * @param mne Hack assembly language mnemonic
     * @return the binary code of the `jump` mnemonic (3 bits as String)
     */
    public String jump(String mne){
        return jumpTable.get(mne);
    }

    /**
     * The translation of Hack Assembly Code's `comp` field to its binary form (bits 6-12 of C-instruction)
     * Map<CompCode, CompBinary>
     */
    private void buildCompTable(){
        this.compTable = new HashMap<>();
        compTable.put("0", "0101010");
        compTable.put("1", "0111111");
        compTable.put("-1", "0111010");
        compTable.put("D", "0001100");
        compTable.put("A", "0110000");
        compTable.put("M", "1110000");
        compTable.put("!D", "0001101");
        compTable.put("!A", "0110001");
        compTable.put("!M", "1110001");
        compTable.put("-D", "0001111");
        compTable.put("-A", "0110011");
        compTable.put("-M", "1110011");
        compTable.put("D+1", "0011111");
        compTable.put("A+1", "0110111");
        compTable.put("M+1", "1110111");
        compTable.put("D-1", "0001110");
        compTable.put("A-1", "0110010");
        compTable.put("M-1", "1110010");
        compTable.put("D+A", "0000010");
        compTable.put("D+M", "1000010");
        compTable.put("D-A", "0010011");
        compTable.put("D-M", "1010011");
        compTable.put("A-D", "0000111");
        compTable.put("M-D", "1000111");
        compTable.put("D&A", "0000000");
        compTable.put("D&M", "1000000");
        compTable.put("D|A", "0010101");
        compTable.put("D|M", "1010101");
    }

    /**
     * The translation of Hack Assembly Code's `dest` field to its binary form (bits 3-5 of C-instruction)
     * Map<DestCode, DestBinary>
     */
    private void buildDestTable(){
        this.destTable = new HashMap<>();
        destTable.put("null", "000");
        destTable.put("M", "001");
        destTable.put("D", "010");
        destTable.put("MD", "011");
        destTable.put("A", "100");
        destTable.put("AM", "101");
        destTable.put("AD", "110");
        destTable.put("AMD", "111");
    }

    /**
     * The translation of Hack Assembly Code's `jump` field to its binary form (bits 0-3 of C-instruction)
     * Map<JumpCode, JumpBinary>
     */
    private void buildJumpTable(){
        this.jumpTable = new HashMap<>();
        jumpTable.put("null", "000");
        jumpTable.put("JGT", "001");
        jumpTable.put("JEQ", "010");
        jumpTable.put("JGE", "011");
        jumpTable.put("JLT", "100");
        jumpTable.put("JNE", "101");
        jumpTable.put("JLE", "110");
        jumpTable.put("JMP", "111");
    }
}
