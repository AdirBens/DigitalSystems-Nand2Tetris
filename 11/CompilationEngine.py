import pathlib

from JackTokenizer import JackTokenizer
from Symbol import Symbol
from SymbolTable import SymbolTable
from Syntax import Syntax
from Token import Token
from VMWriter import VMWriter


class CompilationEngine(object):
    """
    Effects the actual compilation output.
    Gets its input from a JackTokenizer and emits its parsed structure into an output file/stream.
    Output is generated by a series of compilexxx() routines, one for every syntactic element xxx of the Jack grammar.

    The contract between these routines is that each compilexxx() routine should read the syntactic construct xxx from
    the input, advance() the tokenizer exactly beyond xxx, and output the parsing of xxx.
    Thus, compilexxx() may only be called if indeed xxx is the next syntactic element of the input.
    """

    _output_file = None
    _tokenizer = None
    _vmw = None
    _symbol_table = None
    _current_class = None
    current_token = None
    next_token = None

    def __init__(self, output: pathlib.Path, tokenizer: JackTokenizer, debug=False):
        """
        Creates a new compilation engine with the given input and output.
        The next routine called must be compileClass().
        Args:
            output (pathlib.Path) -
        Returns: CompilationEngine object
        """
        self._tokenizer = tokenizer
        self._vmw = VMWriter()
        self.label_counter = 0
        self._debug = debug

    def set_out_file(self, prog_path: pathlib.Path):
        self.close()
        # out_path = prog_path.with_suffix(".xml_debug") if self._debug else prog_path.with_suffix(".xml")
        out_path = prog_path.with_suffix(".debug.vm") if self._debug else prog_path.with_suffix(".vm")
        self._output_file = open(out_path, 'w')
        self._vmw.set_outfile(self._output_file)

    def advance(self) -> None:
        """
        Compile a Complete class
        Returns: None
        """
        # PROBLEM HERE TODO: FIX
        if self.current_token is None:
            if self._tokenizer.has_more_tokens():
                self._tokenizer.advance()
                self.current_token = self._tokenizer.current_token
            if self._tokenizer.has_more_tokens():
                self._tokenizer.advance()
                self.next_token = self._tokenizer.current_token

        elif self._tokenizer.has_more_tokens():
            self.current_token = self.next_token
            self._tokenizer.advance()
            self.next_token = self._tokenizer.current_token

    # TODO: INTEGRATE WITH SYMBOL TABLE
    def compile_class(self) -> None:
        """
        Compiles a static declaration or a field declaration.
        Returns: None
        """
        self._symbol_table = SymbolTable()
        self.advance()
        self.append_tag("<class>", 1)

        self.append_node(self.current_token, 1)  # prints class
        self._current_class = self.append_node(self.current_token, 1)  # prints class_name

        self.append_node(self.current_token, 1)  # prints '{'

        while self.current_token.token_value in {'static', 'field'}:
            self.compile_class_var_dec(2)

        while self.current_token.token_value in {'constructor', 'function', 'method'}:
            self.compile_subroutine_dec(2)

        self.append_node(self.current_token, 1, advance=False)  # prints '}'
        self.append_tag("</class>", 1)

    def compile_class_var_dec(self, indent_lvl: int = 0) -> None:
        """
        Compiles a static declaration or a field declaration.
        Returns: None
        """
        self.append_tag("<classVarDec>", indent_lvl)
        var_symbol = Symbol()
        var_symbol.set_kind(self.append_node(self.current_token, indent_lvl))  # Add Var Kind
        var_symbol.set_type(self.append_node(self.current_token, indent_lvl))  # Add Var Type
        var_symbol.set_name(self.append_node(self.current_token, indent_lvl))  # Add Var Name

        self._symbol_table.add_symbol(var_symbol)
        self.append_symbol(var_symbol, indent_lvl)

        while self.current_token.token_value != ";":
            var_symbol = Symbol(symbol_type=var_symbol.type, symbol_kind=var_symbol.kind)
            if self.current_token.token_value != ',':
                var_symbol.set_name(self.append_node(self.current_token, indent_lvl))
                self._symbol_table.add_symbol(var_symbol)
                self.append_symbol(var_symbol, indent_lvl)
            else:
                self.append_node(self.current_token, indent_lvl)  # prints ","

        self.append_node(self.current_token, indent_lvl)  # prints ";"
        self.append_tag("</classVarDec>", indent_lvl)

    def compile_subroutine_dec(self, indent_lvl: int = 0) -> None:
        """
        Compiles a complete method, function or constructor
        Returns: None
        """
        self.append_tag("<subroutineDec>", indent_lvl)
        self._symbol_table.start_subroutine()

        if self.current_token.token_value == "constructor":
            self._vmw.write_push('constant', self._symbol_table.var_count('field'))
            self._vmw.write_call(class_name='Memory', name='alloc', n_args=1)
            self._vmw.write_pop('pointer', 0)

        if self.current_token.token_value == "method":
            self._vmw.write_push('argument', 0)
            self._vmw.write_pop('pointer', 0)

            this_symbol = Symbol(name="this", symbol_type=self._current_class, symbol_kind="argument")
            self._symbol_table.add_symbol(this_symbol)
            self.append_symbol(this_symbol, indent_lvl)

        self.append_node(self.current_token, indent_lvl)  # prints (method | constructor | function)
        self.append_node(self.current_token, indent_lvl)  # prints (void | type)
        subroutine_name = self.append_node(self.current_token, indent_lvl)  # prints subroutine name

        # PARAMETER LIST
        self.append_node(self.current_token, indent_lvl)  # prints "("
        self.compile_parameter_list(indent_lvl + 1)
        self.append_node(self.current_token, indent_lvl)  # prints ")"

        # SUBROUTINE BODY
        self.compile_subroutine_body(subroutine_name, indent_lvl + 1)
        self.append_tag("</subroutineDec>", indent_lvl)

    def compile_subroutine_body(self,subroutine_name: str, indent_lvl: int = 0) -> None:
        self.append_tag("<subroutineBody>", indent_lvl)

        self.append_node(self.current_token, indent_lvl)  # print "{"

        # VAR DEC
        while self.current_token.token_value == "var":
            self.compile_var_dec(indent_lvl + 1)

        # Compile 'function <subroutine_full_name> <number of arguments>
        self._vmw.write_function(name=subroutine_name, class_name=self._current_class,
                                 l_locals=
                                 # self._symbol_table.var_count("argument") +
                                          self._symbol_table.var_count("local"))

        while self.current_token.token_value != "}":
            # STATEMENTS
            self.compile_statements(indent_lvl + 1)

        self.append_node(self.current_token, indent_lvl)  # print "}"

        self.append_tag("</subroutineBody>", indent_lvl)

    def compile_parameter_list(self, indent_lvl: int = 0) -> None:
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ‘‘()’’.
        Returns: None
        """
        self.append_tag("<parameterList>", indent_lvl)

        while self.current_token.token_value != ")":
            arg_symbol = Symbol(symbol_kind="argument")
            arg_symbol.type = self.append_node(self.current_token, indent_lvl)
            arg_symbol.name = self.append_node(self.current_token, indent_lvl)
            self._symbol_table.add_symbol(arg_symbol)
            self.append_symbol(arg_symbol, indent_lvl)
            if self.current_token.token_value == ",":
                self.append_node(self.current_token, indent_lvl)

        self.append_tag("</parameterList>", indent_lvl)

    def compile_var_dec(self, indent_lvl: int = 0) -> None:
        """
        Compiles a var declaration
        Returns: None
        """
        self.append_tag("<varDec>", indent_lvl)

        var_symbol = Symbol()
        var_symbol.set_kind(
            'local' if self.append_node(self.current_token, indent_lvl) == 'var' else None)  # Add Var Kind
        var_symbol.set_type(self.append_node(self.current_token, indent_lvl))                # Add Var Type
        var_symbol.set_name(self.append_node(self.current_token, indent_lvl))                # Add Var Name

        self._symbol_table.add_symbol(var_symbol)
        self.append_symbol(var_symbol, indent_lvl)

        while self.current_token.token_value != ";":
            var_symbol = Symbol(symbol_type=var_symbol.type, symbol_kind=var_symbol.kind)
            if self.current_token.token_value != ',':
                var_symbol.set_name(self.append_node(self.current_token, indent_lvl))
                self._symbol_table.add_symbol(var_symbol)
                self.append_symbol(var_symbol, indent_lvl)
            else:
                self.append_node(self.current_token, indent_lvl)  # prints ","

        self.append_node(self.current_token, indent_lvl)  # prints ";"
        self.append_tag("</varDec>", indent_lvl)

    def compile_statements(self, indent_lvl: int = 0) -> None:
        """
        Compiles a sequence of statements, not including the enclosing ‘‘{}’’.
        Returns: None
        """
        self.append_tag("<statements>", indent_lvl)

        while self.current_token.token_value in {'let', 'if', 'while', 'do', 'return'}:
            if self.current_token.token_value == "let":
                self.compile_let(indent_lvl + 1)
            elif self.current_token.token_value == "do":
                self.compile_do(indent_lvl + 1)
            elif self.current_token.token_value == "if":
                self.compile_if(indent_lvl + 1)
            elif self.current_token.token_value == "while":
                self.compile_while(indent_lvl + 1)
            elif self.current_token.token_value == "return":
                self.compile_return(indent_lvl + 1)

        self.append_tag("</statements>", indent_lvl)

    def compile_do(self, indent_lvl: int = 0) -> None:
        """
        Compiles a 'do' statement
        Actually implements subroutineCall
        """
        self.append_tag("<doStatement>", indent_lvl)
        self.append_node(self.current_token, indent_lvl)  # prints 'do'

        # SUBROUTINE -
        if self.next_token.token_value in {'.', '('}:
            full_sub_routine_name = None
            #   subroutineName(
            if self.next_token.token_value == '(':
                full_sub_routine_name = self.current_token.token_value                     # subroutineName
                self.append_node(self.current_token, indent_lvl)
            #   OR (className | varName).subroutineName(
            elif self.next_token.token_value == '.':
                full_sub_routine_name = self.append_node(self.current_token, indent_lvl)   # (className | varName)
                full_sub_routine_name += self.append_node(self.current_token, indent_lvl)  # "."
                full_sub_routine_name += self.append_node(self.current_token, indent_lvl)  # subroutineName

            # (EXPRESSION LIST)
            self.append_node(self.current_token, indent_lvl)                               # prints "("
            n_args = self.compile_expression_list(indent_lvl + 1)                          # EXPRESSION LIST
            self.append_node(self.current_token, indent_lvl)                               # prints ")"

            self._vmw.write_call(name=full_sub_routine_name, n_args=n_args)
            self._vmw.write_pop('temp', 0)
        self.append_node(self.current_token, indent_lvl)                                   # prints `;`
        self.append_tag("</doStatement>", indent_lvl)

    def compile_let(self, indent_lvl: int = 0) -> None:
        """
        Compiles a 'let' statement
        Returns: None
        """
        self.append_tag("<letStatement>", indent_lvl)
        self.append_node(self.current_token, indent_lvl)                                # prints "let"
        var_name = self.append_node(self.current_token, indent_lvl)                     # prints varName

        # ARRAY[EXPRESSION] = EXPRESSION
        if self.current_token.token_value == "[":
            self.append_node(self.current_token, indent_lvl)                            # prints "["
            self.compile_expression(indent_lvl + 1)                                     # EXPRESSION
            self.append_node(self.current_token, indent_lvl)                            # prints "]"
            self.append_node(self.current_token, indent_lvl)                            # prints "="
            self._vmw.write_push(segment=self._symbol_table.kind_of(var_name),          # SET POINTER TO ARRAY[INDEX]
                                 index=self._symbol_table.index_of(var_name))
            self._vmw.write_arithmetic('+')

            self.compile_expression(indent_lvl + 1)     # EXPRESSION
            # ARRAY MEM OPERATIONS
            self._vmw.write_pop('temp', 0)              # >> Stores Assigned EXPRESSION Value in 'temp'
            self._vmw.write_pop('pointer', 1)           # >> Set Pointer to point that
            self._vmw.write_push('temp', 0)             # << Get Assigned EXPRESSION Value from 'temp'
            self._vmw.write_pop('that', 0)              # >> Assigning (stores) The value to the Array[index]
        # VAR = EXPRESSION
        else:
            self.append_node(self.current_token, indent_lvl)                            # prints "="
            self.compile_expression(indent_lvl + 1)                                     # EXPRESSION
            self._vmw.write_pop(segment=self._symbol_table.kind_of(var_name),
                                index=self._symbol_table.index_of(var_name))

        self.append_node(self.current_token, indent_lvl)                                # prints ";"
        self.append_tag("</letStatement>", indent_lvl)

    def compile_while(self, indent_lvl: int = 0) -> None:
        """
        Compiles a 'while' statements
        Returns: None
        """
        self.append_tag("<whileStatement>", indent_lvl)
        label_count = self.get_label_counter()

        self.append_node(self.current_token, indent_lvl)            # prints "while"
        self.append_node(self.current_token, indent_lvl)            # prints "("
        self._vmw.write_label("WHILE", label_count)                 # compile label WHILE-X

        self.compile_expression(indent_lvl + 1)                     # EXPRESSION
        self.append_node(self.current_token, indent_lvl)            # prints ")"

        self.append_node(self.current_token, indent_lvl)            # prints "{"
        self._vmw.write_if(f'FALSE{label_count}', is_neg=True)      # compile label False
        self.compile_statements(indent_lvl + 1)                     # STATEMENTS

        self._vmw.write_goto(f'WHILE{label_count}')
        self._vmw.write_label(f'FALSE{label_count}')
        self.append_node(self.current_token, indent_lvl)            # prints "}"
        self.append_tag("</whileStatement>", indent_lvl)

    def compile_return(self, indent_lvl: int = 0) -> None:
        """
        Compiles a 'return' statement
        Returns: None
        """
        self.append_tag("<returnStatement>", indent_lvl)
        self.append_node(self.current_token, indent_lvl)

        print(self.current_token.token_value)
        if self.current_token.token_value != ";":
            self.compile_expression(indent_lvl + 1)

        else:
            self._vmw.write_push("constant", 0)

        self._vmw.write_return()

        self.append_node(self.current_token, indent_lvl)
        self.append_tag("</returnStatement>", indent_lvl)

    def compile_if(self, indent_lvl: int = 0) -> None:
        """
        Compiles an 'if' statement
        Returns: None
        """
        self.append_tag("<ifStatement>", indent_lvl)
        label_count = self.get_label_counter()

        self.append_node(self.current_token, indent_lvl)                        # prints "IF"

        self.append_node(self.current_token, indent_lvl)                        # prints "("
        self.compile_expression(indent_lvl + 1)                                 # EXPRESSION
        self.append_node(self.current_token, indent_lvl)                        # prints ")"

        self.append_node(self.current_token, indent_lvl)                        # prints "{"
        self._vmw.write_if(f'FALSE{label_count}', is_neg=True)
        self.compile_statements(indent_lvl + 1)                                 # STATEMENTS
        self.append_node(self.current_token, indent_lvl)                        # prints "}"

        self._vmw.write_goto(f'END-IF{label_count}')
        self._vmw.write_label(f'FALSE{label_count}')

        # ELSE
        if self.current_token.token_value == "else":
            self.append_node(self.current_token, indent_lvl)                    # prints "else"

            self.append_node(self.current_token, indent_lvl)                    # prints "{"
            self.compile_statements(indent_lvl + 1)                             # STATEMENTS
            self.append_node(self.current_token, indent_lvl)                    # prints "}"

        self._vmw.write_label(f'END-IF{label_count}')
        self.append_tag("</ifStatement>", indent_lvl)

    def compile_expression(self, indent_lvl: int = 0) -> None:
        """
        Compiles an expression
        Returns: None
        """
        self.append_tag("<expression>", indent_lvl)

        # TERM
        self.compile_term(indent_lvl + 1)

        # (OP TERM)*
        while self.current_token.token_value in Syntax.OP:
            op = self.current_token.token_value
            self.append_node(self.current_token, indent_lvl)  # advances to term
            self.compile_term(indent_lvl + 1)  # compiles term
            self._vmw.write_arithmetic(op)  # writes arith op

        self.append_tag("</expression>", indent_lvl)

    def compile_term(self, indent_lvl: int = 0) -> None:
        """
        Compiles a term.
        This routine is faced with a difficulty when trying to decide between some alternative parsing rules.
        Specifically, if the current token is an identifier, the routine must distinguish between a variable,
        an array entry, and a subroutine call. A single look-ahead token, which may be one of ‘‘[’’, ‘‘(’’, or ‘‘.’’
        suffices to distinguish between the three possibilities. Any other token is not part of this term and should
        not be advanced over.
        Returns: None
        """
        self.append_tag("<term>", indent_lvl)

        # if (EXPRESSION)
        if self.current_token.token_value == '(':
            self.append_node(self.current_token, indent_lvl)  # prints "("
            self.compile_expression(indent_lvl + 1)  # compile expression
            self.append_node(self.current_token, indent_lvl)  # prints ")"

        # if unaryOp term
        elif self.current_token.token_value in {'-', '~'}:
            unary_op = self.append_node(self.current_token, indent_lvl)         # prints unary-op
            self.compile_term(indent_lvl + 1)                                   # compile term
            self._vmw.write_arithmetic(unary_op, op_type='unary')               # compile unary-op



        elif self.current_token.token_type == "integerConstant":
            self._vmw.write_integerConst(self.current_token.token_value)
            self.append_node(self.current_token, indent_lvl)

        elif self.current_token.token_type == "stringConstant":
            self._vmw.write_string(self.current_token.token_value)
            self.append_node(self.current_token, indent_lvl)

        elif self.current_token.token_type == "keyword":
            if self.current_token.token_value == "this":
                self._vmw.write_push('pointer', 0)  # compile this
            elif self.current_token.token_value in {'null', 'false', 'true'}:
                self._vmw.write_integerConst(0)  # compile null, false, true
                if self.current_token.token_value == 'true':
                    self._vmw.write_arithmetic('~', op_type='unary')
            self.append_node(self.current_token, indent_lvl)

        # SUBROUTINE -
        elif self.next_token.token_value in {'.', '('}:
            full_sub_routine_name = None
            #   subroutineName(
            if self.next_token.token_value == '(':
                full_sub_routine_name = self.current_token.token_value  # subroutineName
                self.append_node(self.current_token, indent_lvl)
            #   OR (className | varName).subroutineName(
            elif self.next_token.token_value == '.':
                full_sub_routine_name = self.append_node(self.current_token, indent_lvl)  # (className | varName)
                full_sub_routine_name += self.append_node(self.current_token, indent_lvl)  # "."
                full_sub_routine_name += self.append_node(self.current_token, indent_lvl)  # subroutineName

            # (EXPRESSION LIST)
            self.append_node(self.current_token, indent_lvl)  # prints "("
            n_args = self.compile_expression_list(indent_lvl + 1)  # EXPRESSION LIST
            self.append_node(self.current_token, indent_lvl)  # prints ")"

            self._vmw.write_call(name=full_sub_routine_name, n_args=n_args)

        # Array
        elif self.next_token.token_value == '[':
            var_name = self.append_node(self.current_token, indent_lvl)  # var_name
            kind = self._symbol_table.kind_of(var_name)
            index = self._symbol_table.index_of(var_name)

            # EXPRESSION                                                     # push desire Array index
            self.append_node(self.current_token, indent_lvl)  # prints "["
            self.compile_expression(indent_lvl + 1)  # EXPRESSION
            self.append_node(self.current_token, indent_lvl)  # prints "]"

            self._vmw.write_push(kind, index)  # push index of Array head
            self._vmw.write_arithmetic("+")  # push the absolut memory index

        else:  # varName - Must be a Symbol at this stage.
            var_name = self.append_node(self.current_token, indent_lvl)  # var_name
            kind = self._symbol_table.kind_of(var_name)
            index = self._symbol_table.index_of(var_name)
            self._vmw.write_push(kind, index)

        self.append_tag("</term>", indent_lvl)

    def compile_expression_list(self, indent_lvl: int = 0) -> int:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        Returns: number of expressions
        """
        self.append_tag("<expressionList>", indent_lvl)
        n_expression = 0

        if self.current_token.token_value != ')':  # checks if the expressionList is closed
            self.compile_expression(indent_lvl + 1)
            n_expression += 1
            while self.current_token.token_value == ',':
                self.append_node(self.current_token, indent_lvl)  # prints ','
                self.compile_expression(indent_lvl + 1)
                n_expression += 1

        self.append_tag("</expressionList>", indent_lvl)
        return n_expression

    def append_node(self, token: Token, indent_lvl: int = 0, advance: bool = True) -> Token.token_value:
        """
        Write new XMl node to the output file.
        Args:
            token (Token) - a Token object which appends to the XML tree
            indent_lvl (int) - the indentation level represents its hierarchy
            advance (bool) -
        Returns: (bool) true if new xml node append successfully,
                        false in case of the given token is None
        """
        token_value = None
        if token:
            # self._output_file.write('\t' * indent_lvl + token.__str__() + "\n")
            token_value = self.current_token.token_value
            self.advance()
        return token_value

    def append_symbol(self, symbol: Symbol, indent_lvl: int = 0) -> None:
        """
        Write new XMl node to the output file.
        Args:
            token (Token) - a Token object which appends to the XML tree
            indent_lvl (int) - the indentation level represents its hierarchy
            advance (bool) -
        Returns: (bool) true if new xml node append successfully,
                        false in case of the given token is None
        """
        if symbol == "KOOOSHI":
            self._output_file.write('\t' * indent_lvl + symbol.__repr__() + "\n")

    def append_tag(self, tag: str, indent_lvl: int = 0):
        if "Kooshi" == "TRAVOR":
            self._output_file.write((indent_lvl - 1) * "\t" + tag + "\n")

    def compile_subroutine(self):
        pass

    def get_label_counter(self):
        """
        """
        self.label_counter += 1
        return self.label_counter - 1

    def close(self) -> None:
        """
        Closes The Output File
        """
        if self._output_file:
            self._output_file.close()
        if self._symbol_table:
            self._symbol_table.close()
        self.current_token = None
        self.next_token = None
