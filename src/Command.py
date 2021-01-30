import sys


def forward(command, parser):
    parser.turtle.forward(parser.value(command.args))


def backward(command, parser):
    parser.turtle.forward(-parser.value(command.args))


def right(command, parser):
    parser.turtle.rot += parser.value(command.args)


def left(command, parser):
    parser.turtle.rot += -parser.value(command.args)


def setPosition(command, parser):
    parser.turtle.setPos(parser.value(command.args['x']), parser.value(command.args['y']))


def setx(command, parser):
    parser.turtle.setX(parser.value(command.args))


def sety(command, parser):
    parser.turtle.setY(parser.value(command.args))


def home(command, parser):
    parser.turtle.home()


def pendown(command, parser):
    parser.turtle.penDown = True


def penup(command, parser):
    parser.turtle.penDown = False


def setpencolor(command, parser):
    r = parser.value(command.args["r"])
    g = parser.value(command.args["g"])
    b = parser.value(command.args["b"])
    parser.turtle.color = f"rgb({r},{g},{b})"


# Função while
def do_while(command, parser):
    var = command.args["var1"]
    operator = command.args["operator"]
    var2 = command.args["var2"]
    program = command.args["program"]

    var_value = parser.value(var)
    var2_value = parser.value(var2)

    if operator == '<':
        while var_value < var2_value:
            Command.exec(program, parser)
            var_value = parser.value(var)
            var2_value = parser.value(var2)
    elif operator == '>':
        while var_value > var2_value:
            Command.exec(program, parser)
            var_value = parser.value(var)
            var2_value = parser.value(var2)
    elif operator == "=":
        while var_value == var2_value:
            Command.exec(program, parser)
            var_value = parser.value(var)
            var2_value = parser.value(var2)


# Cria a variável
def makevariable(command, parser):
    name = command.args['name']
    parser.vars[name] = parser.value(command.args['value'])


# Função repeat
def repeat(command, parser):
    parser.vars['REPCOUNT'] = 0
    repcount = 0
    num_repeats = parser.value(command.args['num_repeats'])
    program = command.args['program']
    while (repcount < num_repeats):
        Command.exec(program, parser)
        repcount += 1
        parser.vars['REPCOUNT'] = repcount
    parser.vars['REPCOUNT'] = 0


# Verifica as condições, utilizada no if e ifelse.
def check_conditions(command, parser, obj):
    if type(obj) == dict:
        left = check_conditions(command, parser, obj['left'])
        right = check_conditions(command, parser, obj['right'])
        op = obj['op']
        if op == '=':
            return parser.value(obj['left']) == parser.value(obj['right'])
        elif op == '<':
            return parser.value(obj['left']) < parser.value(obj['right'])
        elif op == '>':
            return parser.value(obj['left']) > parser.value(obj['right'])
        elif op == 'and':
            return left and right
        elif op == 'or':
            return left or right


# É utilizada no if e no ifelse
# Enviamos para aqui o programa para correr depois de verificarmos as
# condições.
def rerunProgram(command, parser, program):
    if "name" in program:
        if (program.name == 'repeat'):
            repeat(program, parser)
        elif program.name == 'while':
            do_while(program, parser)
    else:
        command.exec(program, parser)


def do_if(command, parser):
    conditions = command.args['conditions']
    isTrue = check_conditions(command, parser, conditions)
    if isTrue:
        program = command.args['program']
        rerunProgram(command, parser, program)


def do_ifelse(command, parser):
    conditions = command.args['conditions']
    isTrue = check_conditions(command, parser, conditions)
    if isTrue:
        rerunProgram(command, parser, command.args['program_success'])
    else:
        rerunProgram(command, parser, command.args['program_fail'])


def create_func(command, parser):
    name_func = command.args['name_func']
    vars = command.args['vars']
    program = command.args['program']
    parser.funcs[name_func] = {"params": vars, "program": program}


def exec_function(command, parser):
    name_func = command.args['name_func']
    vars = command.args['vars']

    if name_func in parser.funcs:
        func = parser.funcs[name_func]
        params = func['params']
        if len(params) == len(vars):
            backup_vars = parser.vars.copy()
            for var, val in zip(params, vars):
                parser.vars[var] = parser.value(val)
            rerunProgram(command, parser, func['program'])
            parser.vars = backup_vars.copy()
        else:
            print(f'The function {name_func} requires {len(params)} params!', file=sys.stderr)
    else:
        print(f'Error: function {name_func} doesn\'t exist!', file=sys.stderr)


class Command:
    def __init__(self, command, args=None):
        self.name = command
        self.args = args

    def __repr__(self):
        return f"Command({self.name}, {self.args})"

    dispatch_table = {"fd": forward, "bk": backward, "rt": right, "lt": left,
                      "setpos": setPosition, "setx": setx, "sety": sety,
                      "pendown": pendown, "penup": penup, "setpencolor": setpencolor, "while": do_while,
                      "make": makevariable, "repeat": repeat, "if": do_if, "ifelse": do_ifelse,
                      "create_func": create_func, "exec_function": exec_function}

    def runProgram(self, parser):
        self.dispatch_table[self.name](self, parser)


    @classmethod
    def exec(cls, program, parser):
        for command in program:
            command.runProgram(parser)
