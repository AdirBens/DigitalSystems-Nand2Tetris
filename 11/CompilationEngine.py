from pathlib import Path

from JackTokenizer import JackTokenizer
from Symbol import Symbol
from Syntax import Syntax
from VMWriter import VMWriter
from SymbolTable import SymbolTable


class CompilationEngine(object):
    """
    Effects the actual compilation output.
    Gets its input from a JackTokenizer and emits its parsed structure into an output file/stream.
    Output is generated by a series of compilexxx() routines, one for every syntactic element xxx of the Jack grammar.

    The contract between these routines is that each compilexxx() routine should read the syntactic construct xxx from
    the input, advance() the tokenizer exactly beyond xxx, and output the parsing of xxx.
    Thus, compilexxx() may only be called if indeed xxx is the next syntactic element of the input.
    """
    def __init__(self, tokenizer: JackTokenizer, debug: bool = False):
        """
        Creates a new compilation engine with the given input and output.
        The next routine called must be compileClass().
        Args: output (Path) - Path to where output file should be created
              debug (bool)  - create debug file, do not override cmp files
        Returns: CompilationEngine object
        """
        self.debug = debug
        self._out_file = None
        self._tokenizer = tokenizer
        self._vmw = VMWriter()
        self._symbol_table = None

        self._current_class = None
        self._label_counter = 0

        self.current_token = None
        self.next_token = None

    def set_out_file(self, program_path: Path) -> None:
        """
        Creates and open new .vm file and Sets Engin's out_file to this file
            Also sets the VMWriter out file to be as the new Engin's out-file
        Args: program_path (Path) - path of the current compiled .jack file
        """
        # self.close()
        new_outfile = program_path.with_suffix(".debug.vm") if self.debug else program_path.with_suffix(".vm")
        self._out_file = open(new_outfile, 'w')
        self._vmw.set_outfile(self._out_file)

    def advance(self, skips: int = 1) -> list[str]:
        """
        Handles current_token and next_token reading by invoke JackTokenizer.advance()
        Args: [OPTIONAL] skips (int) - number of tokens to skip, after skipping, the current_token sets to be the
                                       current_token + skips token.
        Returns: advanced_values (list) - list of current_token.values() advanced.
        """
        advanced_values = []
        skips = skips + 2 if self.current_token is None else skips  # in case of first advance

        for _ in range(skips):
            if self._tokenizer.has_more_tokens():
                if self.current_token is not None:  # skips current_token before the first advance
                    advanced_values.append(self.current_token.token_value)
                self._tokenizer.advance()
                self.current_token = self.next_token
                self.next_token = self._tokenizer.current_token

        return advanced_values

    def compile_class(self) -> None:
        """
        Compile a Complete class - in particular, compile .jack file
        """
        self._symbol_table = SymbolTable()
        self._current_class = self.advance(skips=3)[1]       # Skips 'class', get current class name and skips '{'

        while self.current_token.token_value in {'static', 'field'}:
            self.compile_var_dec(force_kind=False)

        while self.current_token.token_value in {'constructor', 'function', 'method'}:
            self.compile_subroutine_dec()

        self.advance()  # Skips '}'

    def compile_var_dec(self, force_kind: bool = True) -> None:
        """
        Compiles a static declaration or a field declaration.
        Args: [OPTIONAL] force_kind (bool; default = True) - Useful in general var declaration
              if var.kind == 'var' set var.kind = 'local', else set var.kind = 'none'
        """
        # Reads kind type name and init new symbol
        var_symbol = Symbol(*self.advance(skips=3))
        if force_kind:
            var_symbol.set_kind('local' if var_symbol.kind == 'var' else None)
        self._symbol_table.add_symbol(var_symbol)

        while self.current_token.token_value != ';':
            var_symbol = Symbol(symbol_type=var_symbol.type, symbol_kind=var_symbol.kind)
            if self.current_token.token_value != ',':
                var_symbol.set_name(self.advance()[0])
                self._symbol_table.add_symbol(var_symbol)
            else:
                self.advance()  # Skips ','
        self.advance()          # Skips ';'

    def compile_subroutine_dec(self) -> None:
        """
        Compiles a complete `method`, `function` or `constructor`
        """
        self._symbol_table.start_subroutine()
        # Reads (method | constructor | function) (void | type) subroutineName
        subroutine_kind, subroutine_type, subroutine_name = self.advance(skips=3)

        if subroutine_kind == "method":
            this_symbol = Symbol(symbol_kind="argument", symbol_type=self._current_class, name="this")
            self._symbol_table.add_symbol(this_symbol)

        # (PARAMETER LIST)
        self.advance()                      # Skips '('
        self.compile_parameter_list()       # PARAMETER LIST
        self.advance()                      # Skips ')'
        # SUBROUTINE BODY
        self.compile_subroutine_body(subroutine_name, subroutine_type)

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ‘()’.
        """
        while self.current_token.token_value != ')':
            arg_symbol_type, arg_symbol_name = self.advance(skips=2)
            arg_symbol = Symbol(symbol_kind="argument", symbol_type=arg_symbol_type, name=arg_symbol_name)
            self._symbol_table.add_symbol(arg_symbol)

            if self.current_token.token_value == ',':
                self.advance()

    def compile_subroutine_body(self, subroutine_name: str, subroutine_type: str) -> None:
        """
        Compile Subroutine body section - { VAR DEC } STATEMENTS
        Args: subroutine_name (str) - the name of this subroutine
              subroutine_type (str) - the return type of this subroutine
        """
        self.advance()  # Skips '{'

        while self.current_token.token_value == "var":      # VAR DEC
            self.compile_var_dec()

        # Compile 'function <subroutine_full_name> <number of arguments>
        self._vmw.write_function(name=subroutine_name, class_name=self._current_class,
                                 l_locals=self._symbol_table.var_count("local"))
        if subroutine_type == "constructor":    # Memory Allocation and initialize new object
            self._vmw.write_push(segment='constant', index=self._symbol_table.var_count("field"))
            self._vmw.write_call(name='alloc', class_name='Memory', n_args=1)
            self._vmw.write_pop(segment='pointer', index=0)
        elif subroutine_type == "method":
            self._vmw.write_push(segment='argument', index=0)
            self._vmw.write_pop(segment='pointer', index=0)

        while self.current_token.token_value != '}':    # STATEMENTS
            self.compile_statements()

        self.advance()  # Skips '}'

    def compile_statements(self) -> None:
        """
        Compiles a sequence of statements, not including the enclosing ‘{}’.
        """
        while self.current_token.token_value in {'let', 'if', 'while', 'do', 'return'}:
            if self.current_token.token_value == "let":
                self.compile_let()
            elif self.current_token.token_value == "do":
                self.compile_do()
            elif self.current_token.token_value == "if":
                self.compile_if()
            elif self.current_token.token_value == "while":
                self.compile_while()
            elif self.current_token.token_value == "return":
                self.compile_return()

    def compile_let(self) -> None:
        """
        Compiles a 'let' statement
        """
        var_name = self.advance(skips=2)[1]   # Reads 'let varName'

        #  ARRAY[EXPRESSION] = EXPRESSION
        if self.current_token.token_value == '[':
            self.advance()                      # Skips '['
            self.compile_expression()           # EXPRESSION
            self.advance(skips=2)               # Skips '] = '
            # Set Pointer to ARRAY[INDEX]
            self._vmw.write_push(segment=self._symbol_table.kind_of(var_name),
                                 index=self._symbol_table.index_of(var_name))
            self._vmw.write_arithmetic('+')
            # Eval the assigned EXPRESSION
            self.compile_expression()
            # Assignment of Array[index] = EXPRESSION
            self._vmw.write_pop(segment='temp', index=0)     # >> Stores Assigned EXPRESSION Value in 'temp'
            self._vmw.write_pop(segment='pointer', index=1)  # >> Set Pointer to point that
            self._vmw.write_push(segment='temp', index=0)    # << Get Assigned EXPRESSION Value from 'temp'
            self._vmw.write_pop(segment='that', index=0)     # >> Assigning (stores) The value to the Array[index]
        # VAR = EXPRESSION
        else:
            self.advance()              # Skips '='
            self.compile_expression()   # EXPRESSION
            self._vmw.write_pop(segment=self._symbol_table.kind_of(var_name),
                                index=self._symbol_table.index_of(var_name))
        self.advance()  # Skips ';'

    def compile_do(self) -> None:
        """
        Compiles a 'do' statement (Actually implements subroutineCall)
        """
        self.advance()                                  # Skips 'do'
        # SUBROUTINE
        self._compile_subroutine_call()                 # Compile subroutine call
        self._vmw.write_pop(segment='temp', index=0)    # Clear Garbage
        self.advance()                                  # Skips ';'

    def compile_if(self) -> None:
        """
        Compiles an 'if' statement
        """
        label_count = self.get_label_counter()
        self.advance(skips=2)                                              # Skips 'if ('
        self.compile_expression()                                          # EXPRESSION
        self.advance(skips=2)                                              # Skips ') {'
        self._vmw.write_if(f'FALSE{label_count}', is_neg=True)
        self.compile_statements()                                          # STATEMENTS
        self.advance()                                                     # Skips '}'
        self._vmw.write_goto(f'END-IF{label_count}')
        self._vmw.write_label(f'FALSE{label_count}')
        # ELSE
        if self.current_token.token_value == "else":
            self.advance(skips=2)                                          # Skips 'else {'
            self.compile_statements()                                      # STATEMENTS
            self.advance()                                                 # Skips '}'
        self._vmw.write_label(f'END-IF{label_count}')

    def compile_while(self) -> None:
        """
        Compiles a 'while' statements
        """
        label_count = self.get_label_counter()
        self.advance(skips=2)                                             # Skips 'while ('
        self._vmw.write_label('WHILE', label_count)
        self.compile_expression()                                         # EXPRESSION

        self.advance(skips=2)                                             # Skips ') {'
        self._vmw.write_if(f'FALSE{label_count}', is_neg=True)            # IF LABEL
        self.compile_statements()                                         # STATEMENTS

        self._vmw.write_goto(f'WHILE{label_count}')
        self._vmw.write_label(f'FALSE{label_count}')
        self.advance()                                                    # Skips '}'

    def compile_return(self) -> None:
        """
        Compiles a 'return' statement
        """
        self.advance()

        if self.current_token.token_value != ';':
            self.compile_expression()   # EXPRESSION
        else:
            self._vmw.write_push(segment='constant', index=0)

        self._vmw.write_return()
        self.advance()

    def compile_expression(self) -> None:
        """
        Compiles an expression
        """
        self.compile_term()                                     # TERM

        while self.current_token.token_value in Syntax.OP:      # (OP TERM) *
            op = self.current_token.token_value
            self.advance()                   # Advance to term
            self.compile_term()              # Compile term
            self._vmw.write_arithmetic(op)   # Writes arithmetic op

    def compile_term(self) -> None:
        """
        Compiles a term.
        This routine is faced with a difficulty when trying to decide between some alternative parsing rules.
        Specifically, if the current token is an identifier, the routine must distinguish between a variable,
        an array entry, and a subroutine call. A single look-ahead token, which may be one of ‘[’, ‘(’, or ‘.’
        suffices to distinguish between the three possibilities. Any other token is not part of this term and should
        not be advanced over.
        """
        # (EXPRESSION)
        if self.current_token.token_value == '(':
            self.advance()                  # Skips "("
            self.compile_expression()       # compile expression
            self.advance()                  # Skips ")"
        # UnaryOperation TERM
        elif self.current_token.token_value in {'-', '~'}:
            unary_op = self.advance()[0]                             # Skips unary-op
            self.compile_term()                                      # compile term
            self._vmw.write_arithmetic(unary_op, op_type='unary')    # compile unary-op
        # integerConstant TERM
        elif self.current_token.token_type == 'integerConstant':
            self._vmw.write_integer_const(const=self.current_token.token_value)
            self.advance()
        # stringConstant TERM
        elif self.current_token.token_type == 'stringConstant':
            self._vmw.write_string(self.current_token.token_value)
            self.advance()
        # SUBROUTINE
        elif self.next_token.token_value in {'.', '('}:
            self._compile_subroutine_call()
        # KEYWORDS
        elif self.current_token.token_type == "keyword":
            if self.current_token.token_value == "this":
                self._vmw.write_push(segment='pointer', index=0)                # compile this
            elif self.current_token.token_value in {'null', 'false', 'true'}:
                self._vmw.write_integer_const(0)                                 # compile null, false, true
                if self.current_token.token_value == 'true':
                    self._vmw.write_arithmetic('~', op_type='unary')
            self.advance()
        # Array
        elif self.next_token.token_value == '[':
            var_name = self.advance()[0]                    # Get var_name
            kind = self._symbol_table.kind_of(var_name)
            index = self._symbol_table.index_of(var_name)

            # EXPRESSION - push desire Array index
            self.advance()                                  # Skips "["
            self.compile_expression()                       # EXPRESSION
            self.advance()                                  # Skips "]"
            self._vmw.write_push(segment=self._symbol_table.kind_of(var_name),
                                 index=self._symbol_table.index_of(var_name))
            self._vmw.write_arithmetic("+")                 # push the absolut memory index
            self._vmw.write_pop('pointer', 1)
            self._vmw.write_push('that', 0)
        # varName - Must be a Symbol at this stage.
        else:
            var_name = self.advance()[0]
            self._vmw.write_push(segment=self._symbol_table.kind_of(var_name),
                                 index=self._symbol_table.index_of(var_name))

    def compile_expression_list(self) -> int:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        Returns: (int) number of expressions
        """
        n_expression = 0

        if self.current_token.token_value != ')':  # checks if the expressionList is closed
            self.compile_expression()
            n_expression += 1
            while self.current_token.token_value == ',':
                self.advance()  # Skips '.'
                self.compile_expression()
                n_expression += 1

        return n_expression

    def close(self) -> None:
        """
        Closes The Output File, and Resets fields
        """
        if self._out_file:
            self._out_file.close()
        if self._symbol_table:
            self._symbol_table.close()
        self.current_token, self.next_token = None, None

    # AUXILIARY FUNCTIONS
    def _compile_subroutine_call(self) -> int:
        """
        Compile Subroutine Call determines kind of subroutine and produced code that
        prepare memory segments to subroutine call.
        Returns: (int) number of arguments (n_args)
        """
        is_method = True
        name = self.current_token.token_value
        class_name = self._current_class
        n_args = 0

        #   OR (className | varName).subroutineName(
        if self.next_token.token_value == '.':
            is_method = False
            # Read (className | varName) ".", and checks if current token value is a symbol
            is_symbol = self._symbol_table.get_symbol(self.advance(skips=2)[0])
            name = self.current_token.token_value
            if is_symbol:
                n_args = 1
                self._vmw.write_push(segment=self._symbol_table.kind_of(class_name),
                                     index=self._symbol_table.index_of(class_name))
                class_name = self._symbol_table.type_of(class_name)
        # subroutineName(
        if self.next_token.token_value == '(':
            self.advance()      # Advance to '('
            if is_method:
                n_args = 1
                self._vmw.write_push(segment='pointer', index=0)
            # (EXPRESSION LIST)
            self.advance()      # Skips '('
            n_args += self.compile_expression_list()    # EXPRESSION LIST
            self._vmw.write_call(name=f'{class_name}.{name}', n_args=n_args)
            self.advance()      # Skips ')'

        return n_args

    def get_label_counter(self) -> int:
        """
        Returns: (int) Labels counter in Ascending sequence
        """
        self._label_counter += 1
        return self._label_counter - 1

    def __str__(self):
        header = "[CompileEngine] "
        delimiter = "\n" + (max(len(header), 8) * " ")
        return f"{header}outFile - {self._out_file}{delimiter}current_class - {self._current_class}{delimiter}" \
               f"current_token - {self.current_token}  |  next_token - {self.next_token}"
