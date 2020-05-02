import math
import operator

OPERATORS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

MATH_FUNCS = {
    'sin': math.sin,
    'cos': math.cos,
    'tg': math.tan,
    'ln': math.log,
    'fact': math.factorial,
    'exp': math.exp
}


def calc_logic(token):
    try:
        return float(token)
    except ValueError:
        begin = token.find('(')
        if begin == 0 and token[-1] == ')':
            return parse(token[1:-1])

        elif begin > 0 and token[-1] == ')':
            name = token[0:begin]
            arg = parse(token[begin+1: -1])
            result = MATH_FUNCS[name](arg)
            return result
        else:
            raise ValueError(f'Unknown token {repr(token)}')


def parse(text):
    token = ''
    depth = 0
    current_operator = None
    current_value = None

    def close_token():
        nonlocal token, current_operator, current_value
        if token != '':
            if current_value is None:
                current_value = calc_logic(token)
            else:
                current_value = OPERATORS[current_operator](current_value, calc_logic(token))
                current_operator = None
            token = ''

    for item in text:
        if depth > 0:
            if item == ' ':
                continue
            token += item
            if item == ')':
                depth -= 1
                close_token()

        elif item == '(':
            if token == '':
                close_token()
            depth += 1
            token += item

        else:
            if item == ' ':
                continue
            elif item in OPERATORS:
                close_token()
                current_operator = item
            else:
                token += item

    close_token()
    return current_value
