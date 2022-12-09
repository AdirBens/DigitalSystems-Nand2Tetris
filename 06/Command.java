import java.util.regex.Pattern;

/**
 * Command types and their valid patterns
 * <p>
 * Be aware of the fact that L pattern is private case of C Pattern -
 * (!)(!)(!) DO NOT CHANGE Command Enum INNER ORDER (!)(!)(!)
 */
enum Command{
    EMPTY(Pattern.compile("^$")),
    COMMENT(Pattern.compile("(^//.*$)")),
    L_COMMAND(Pattern.compile("^\\((.*)\\)$")),
    A_COMMAND(Pattern.compile("^@(.*)$")),
    C_COMMAND(Pattern.compile("((^[ADM]{0,3})=)?([01ADM!-]?[-+&|]?[01ADM])(;(J[EGLMN][TQEP]$))?"));

    public final Pattern pattern;
    Command(Pattern commandPattern){
        pattern = commandPattern;
    }
}