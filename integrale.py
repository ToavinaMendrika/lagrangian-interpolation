from sympy import *


x = symbols('x')
print( integrate(x**2 * exp(x) * cos(x), x) )