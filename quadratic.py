# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        return "( )"
    elif discriminante == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        r1 = (-b + discriminante**0.5) / (2 * a)
        r2 = (-b - discriminante**0.5) / (2 * a)
        return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0 and c == 0:
        return f"f(x) = {b} * X"
    elif b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"



def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
