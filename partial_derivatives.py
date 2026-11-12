from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')

f = 2 * x ** 3 + 3 * y ** 3

dx_f = diff(f, x)
dy_f = diff(f, y)

f2 = dx_f + 3 * y ** 3

plot3d(f)
plot3d(f2)