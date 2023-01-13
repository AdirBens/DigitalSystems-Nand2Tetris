import re


class Syntax(object):
    """
    The Jack language syntax
    """
    TERMINALS = {
        'inlineComment': re.compile("//.\\*"),

        'symbol': re.compile("{|}|[(]|[)]|\\[|\\]|[|]|[.]|,|[;]|\\+|-|\\*|/|&|\\||<|>|=|~"),

        'keyword': re.compile("class|constructor|function|method|field|static|var"
                              "|int|char|boolean|void|true|false|null|"
                              "this|let|do|if|else|return|while(?=\\W)"),

        'integerConstant': re.compile("^[0-9]+"),

        'stringConstant': re.compile("^\"([^\\n\"]+)\""),

        'identifier': re.compile("^[a-zA-Z_]+\\w*")
    }

