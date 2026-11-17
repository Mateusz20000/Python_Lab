from sympy import *
import cmath


x = symbols('x')

f = x**2 + 1

Sfdx = integrate(f, (x, 0, 1)) #całka oznaczona
print(Sfdx)

plot(f, Sfdx)