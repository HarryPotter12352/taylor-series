from sympy import symbols, diff, exp, I, factorial
import math
x, y = symbols('x y')
f = exp(x)
n = 100
a = math.pi
point_to_evaluate = math.pi*I
funcs = [f]
for i in range(1, n+1):
    f = diff(f, x)
    funcs.append(f)
factorials = [factorial(i) for i in range(n)]
output = [((funcs[i].subs(x, a))/factorials[i])*((y-a)**i) for i in range(n)]
final = sum(output)
print(final.subs(y, point_to_evaluate).evalf())