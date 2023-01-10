"""
JackCompiler Errors
"""


class JackSyntaxError(Exception):
    """
    Jack Syntax Error - Syntx violation encounter while tokenize or parse jack program
    """
    pass


class JackCompilationError(Exception):
    pass


class InvalidInputFileError(Exception):
    pass

