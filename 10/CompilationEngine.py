import pathlib


class CompilationEngine(object):
    """
    Effects the actual compilation output. Gets its input from a JackTokenizer and emits its parsed structure
    into an output file/stream. The output is generated by a series of compilexxx() routines, one for every syntactic
    element xxx of the Jack grammar.
    The contract between these routines is that each compilexxx() routine should read the syntactic construct xxx from
    the input, advance() the tokenizer exactly beyond xxx, and output the parsing of xxx. Thus, compilexxx() may only
    be called if indeed xxx is the next syntactic element of the input.
    """

    INPUT_FILE = None
    OUTPUT_FILE = None

    def __init__(self, output: pathlib.Path):
        """
        Creates a new compilation engine with the given input and output.
        The next routine called must be compileClass().
        Args:
            output (pathlib.Path) -
        Returns: CompilationEngine object
        """
        self.OUTPUT_FILE = output

    def set_input_file(self, input_file: str) -> None:
        """
        Sets this CompilationEngine INPUT FILE to a given input_file
        Args:
            input_file (str) -
        Returns: None
        """
        self.INPUT_FILE = input_file

    def compile_class(self) -> None:
        """
        Compile a Complete class
        Returns: None
        """
        pass

    def compile_class_var_dec(self) -> None:
        """
        Compiles a static declaration or a field declaration.
        Returns: None
        """
        pass

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function or constructor
        Returns: None
        """
        pass

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ‘‘()’’.
        Returns: None
        """
        pass

    def compile_var_dec(self) -> None:
        """
        Compiles a var declaration
        Returns: None
        """
        pass

    def compile_statement(self) -> None:
        """
        Compiles a sequence of statements, not including the enclosing ‘‘{}’’.
        Returns: None
        """
        pass

    def compile_do(self) -> None:
        """
        Compiles a 'do' statement
        Returns: None
        """
        pass

    def compile_let(self) -> None:
        """
        Compiles a 'let' statement
        Returns: None
        """
        pass

    def compile_while(self) -> None:
        """
        Compiles a 'while' statements
        Returns: None
        """
        pass

    def compile_return(self) -> None:
        """
        Compiles a 'return' statement
        Returns: None
        """
        pass

    def compile_if(self) -> None:
        """
        Compiles an 'if' statement
        Returns: None
        """
        pass

    def compile_expression(self) -> None:
        """
        Compiles an expression
        Returns: None
        """
        pass

    def compile_term(self) -> None:
        """
        Compiles a term.
        This routine is faced with a difficulty when trying to decide between some alternative parsing rules.
        Specifically, if the current token is an identifier, the routine must distinguish between a variable,
        an array entry, and a subroutine call. A single look-ahead token, which may be one of ‘‘[’’, ‘‘(’’, or ‘‘.’’
        suffices to distinguish between the three possibilities. Any other token is not part of this term and should
        not be advanced over.
        Returns: None
        """
        pass

    def compile_expression_list(self) -> None:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        Returns: None
        """
        pass
