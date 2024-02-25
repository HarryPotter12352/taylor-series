from sympy import symbols, diff
import math
x = symbols('x')
y = symbols('y')
f = math.e**(2*x)
n = 20
a = math.pi
point_to_evaluate = 2
funcs = [f]
output = []
for i in range(1,n+1):
    f_prime = f # f' = f
    for j in range(1,i+1):
        f_prime = diff(f_prime,x)
    funcs.append(f_prime)
for i in range(n):
    output.append(((funcs[i].subs(x,a))/math.factorial(i))*((y-a)**i))
final = 0
for i in output:
    final += i
print(final.subs(y,point_to_evaluate))