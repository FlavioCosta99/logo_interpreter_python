import ply.lex as lex
import sys

comp_table = {"forward": "fd", "back": "bk", "left": "lt", "right": "rt",
              "pendown": "pd", "penup": "pu"}


class Lexer:
    tokens = ("FLOAT", "VAR", "fd", "bk", "lt", "rt",
              "setpos", "setxy", "setx", "sety", "home", "pd",
              "pu", "setpencolor", "make", "while", "repeat",
              "ifelse", "if", "STR", "to", "end", "and", "or")

    literals = "[],><*+-/=()&&"
    t_ignore = " \n\t"

    def t_COMMAND(self, t):
        r"fd|forward|bk|back|lt|left|rt|right|setpos|setxy|setx|sety|home|pendown|pd|penup|pu|setpencolor|make|while|repeat|ifelse|if|to|end|and|or"
        if t.value in comp_table:
            t.type = comp_table[t.value]
        else:
            t.type = t.value

        return t

    def t_FLOAT(self, t):
        r"""[+-]?([0-9]+[.])?[0-9]+"""
        t.value = float(t.value)
        return t

    def t_VAR(self, t):
        r""" [":][a-zA-Z0-9]+ """
        t.value = t.value[1:]
        return t

    def t_STR(self, t):
        r""" [a-zA-Z0-9]+"""
        return t

    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
        self.lexer = None

    def Build(self, input, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.input(input)
