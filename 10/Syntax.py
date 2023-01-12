import re


class Syntax(object):
    """

    """
    # TODO: take a look of CPython Tokenizer https://github.com/python/cpython/blob/v3.7.4/Lib/tokenize.py
    # TERMINALS = {
    #     # 'keyword': re.compile("(class)\\W|(constructor)\\W|(function)\\W|(method)\\W|"
    #     #                       "(field)\\W|(static)\\W|(var)\\W|(int)\\W|(char)\\W|"
    #     #                       "(boolean)\\W|(void)\\W|(true)\\W|(false)\\W|(null)\\W|"
    #     #                       "(this)\\W|(let)\\W|(do)\\W|(if)\\W|(else)\\W|\\W*(return)\\W|(while)\\W"),
    #
    #

    TERMINALS = {
        'keyword': re.compile("([class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|"
                              "this|let|do|if|else|return|while])[{|}|[(]|[)]|\\[|\\]|[|]|[.]|,|[;]|\\+|-|\\*|/|&|\\||<|>|=|~| | \\t]?"),

        'symbol': re.compile("{|}|[(]|[)]|\\[|\\]|[|]|[.]|,|[;]|\\+|-|\\*|/|&|\\||<|>|=|~"),

        'integer_constant': re.compile("^[0-9]+"),

        'string_constant': re.compile("^\"([^\\n\"]+)\""),

        'identifier': re.compile("^[a-zA-Z_]+\\w*"),

        'inline_comment': re.compile("//.\\*")
    }

    Comments = {
        'startline': re.compile("^//"),
        'open_multiline': re.compile("^/\\*"),
        'end_multiline': re.compile("\\*/$")
    }
