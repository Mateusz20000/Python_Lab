from sympy import *


x = symbols('x')


def taylor_series(fun, a, n: int):

    r_fun = 0

    for i in range(n+1):
        r_fun += ( fun.subs(x, a) * ( x - a )**i ) / ( factorial(i) )
        fun = diff(fun)

    return r_fun


T_sin = taylor_series(sin(x), 0, 7)

if T_sin == x - x**3/6 + x**5/120: print(True)

print(T_sin.subs(x, 1).evalf())
print(sin(1).evalf())
