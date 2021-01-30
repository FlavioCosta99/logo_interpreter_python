from src.Lexer import Lexer
import ply.yacc as yacc
import sys
from src.Turtle import Turtle
from src.Command import Command


class Parser:
    tokens = Lexer.tokens
    precedence = (
        ("left", 'or'),
        ("left", 'and'),
        ("left", '+', '-'),
        ("left", '*', '/'),
    )

    def __init__(self):
        self.parser = None
        self.lexer = None
        self.turtle = None
        self.funcs = {}
        self.vars = {}

    def value(self, val):
        if type(val) == dict and "op" in val:
            left = self.value(val["left"])
            right = self.value(val["right"])
            op = val["op"]
            if op == "+":
                return left + right
            elif op == "*":
                return left * right
            elif op == "-":
                return left - right
            elif op == "/":
                if right == 0:
                    print("Division by zero", file=sys.stderr)
                    exit(1)
                return left / right
            else:
                print(f"Unknown operator: {op}", file=sys.stderr)

        if type(val) == int or type(val) == float:
            return val
        if val in self.vars:
            return self.vars[val]
        print(f"Variable: {val} undefined", file=sys.stderr)
        self.vars[val] = 0
        return False

    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        self.turtle = Turtle()
        program = self.parser.parse(lexer=self.lexer.lexer)
        Command.exec(program, self)
        self.end()

    def end(self):
        self.turtle.file = f"<svg xmlns='http://www.w3.org/2000/svg'>\n" + self.turtle.file + "</svg>"
        self.turtle.save()
        exit(1)

    def p_error(self, t):
        print(f"Syntax error: {t}", file=sys.stderr)
        exit(1)

    def p_program0(self, p):
        """ program :  command """
        p[0] = [p[1]]

    def p_program1(self, p):
        """ program : program command """
        lst = p[1]
        lst.append(p[2])
        p[0] = lst

    def p_forward(self, p):
        """ command : fd value"""
        p[0] = Command("fd", p[2])

    def p_back(self, t):
        """ command : bk value"""
        t[0] = Command("bk", t[2])

    def p_right(self, t):
        """ command : rt value"""
        t[0] = Command("rt", t[2])

    def p_left(self, t):
        """ command : lt value """
        t[0] = Command("lt", t[2])

    def p_setpos(self, t):
        """ command : setpos '[' value value ']' """
        t[0] = Command("setpos", {"x": t[3], "y": t[4]})

    def p_setxy(self, t):
        """ command : setxy value value """
        t[0] = Command("setpos", {"x": t[2], "y": t[3]})

    def p_setx(self, t):
        """ command : setx value"""
        t[0] = Command("setx", t[2])

    def p_sety(self, t):
        """ command : sety value"""
        t[0] = Command("sety", t[2])

    def p_home(self, t):
        """ command : home"""
        t[0] = Command("home")

    def p_pd(self, t):
        """ command : pd"""
        t[0] = Command("pendown")

    def p_pu(self, t):
        """ command : pu"""
        t[0] = Command("penup")

    def verifyRgb(self, value, variable):
        if type(value) == float and value > 255:
            print(f"Warning: {variable} must be lower than 255. Using 255 instead. ", file=sys.stderr)
            return 255
        elif type(value) == float and value < 0:
            print(f"Warning: {variable} must be higher than 0. Using 0 instead. ", file=sys.stderr)
            return 0
        else:
            return value

    def p_setpencolor(self, t):
        """ command : setpencolor '[' value value value ']' """
        t[3] = self.verifyRgb(t[3], 'r')
        t[4] = self.verifyRgb(t[4], 'g')
        t[5] = self.verifyRgb(t[5], 'b')
        t[0] = Command("setpencolor", {"r": t[3], "g": t[4], "b": t[5]})

    def p_make(self, t):
        """ command : make VAR value """
        t[0] = Command("make", {"name": t[2], "value": t[3]})

    def p_while(self, t):
        """ command : while '[' value operator value ']' '[' program ']'   """
        t[0] = Command("while", {"var1": t[3], "operator": t[4],
                                 "var2": t[5], "program": t[8]})

    def p_repeat(self, t):
        """ command : repeat value '[' program ']' """
        t[0] = Command("repeat", {"num_repeats": t[2], "program": t[4]})

    def p_value(self, t):
        """  value  :   FLOAT
                    |   VAR
                    |   '(' value ')'
                    |   value operations value """
        if len(t) == 4:
            if t[1] == '(':
                t[0] = t[2]
            else:
                t[0] = {'left': t[1], 'right': t[3], 'op': t[2]}
        elif len(t) == 2:
            t[0] = t[1]

    def p_operator(self, p):
        """ operator : '>'
                    | '<'
                    | '=' """
        p[0] = p[1]

    def p_operations(self, p):
        """ operations : '*'
                       | '-'
                       | '+'
                       | '/' """
        p[0] = p[1]

    def p_if(self, p):
        """ command : if comparation '[' program ']' """
        p[0] = Command("if", {"conditions": p[2], "program": p[4]})

    def p_ifelse(self, p):
        """ command : ifelse comparation '[' program ']' '[' program ']' """
        p[0] = Command("ifelse", {"conditions": p[2], "program_success": p[4], "program_fail": p[7]})

    def p_comparation(self, t):
        """ comparation : value operator value
                        | comparation and comparation
                        | comparation or comparation """
        if len(t) == 4:
            t[0] = {"left": t[1], "op": t[2], "right": t[3], }

    def p_varlist(self, p):
        """ varlist :
                   | VAR
                   | varlist VAR """
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[2])

    def p_to(self, p):
        """  command : to STR varlist program end"""
        p[0] = Command('create_func', {"name_func": p[2], "vars": p[3], "program": p[4]})


    def p_callfunc(self, p):
        """ command : STR inc_value """
        p[0] = Command('exec_function', {"name_func": p[1], "vars": p[2]})

    def p_inc_value(self, p):
        """ inc_value :
                      | value
                      | inc_value value """
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 3:
            p[0] = p[1]
            p[0].append(p[2])
