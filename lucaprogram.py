from sympy import *

x = symbols("x")

var_a = float(input("What is variable a? "))
var_b = float(input("What is variable b? "))
var_c = float(input("What is variable c? "))
comparator = input("How would you like to compare the function? Enter >, <, >=, or <=: ")

if comparator == ">":
    print(solve(var_a * x**2 + var_b * x + var_c > 0))
elif comparator == ">=":
    print(solve(var_a * x ** 2 + var_b * x + var_c >= 0))
elif comparator == "<":
    print(solve(var_a * x ** 2 + var_b * x + var_c < 0))
else:
    print(solve(var_a * x ** 2 + var_b * x + var_c <= 0))

vertex_x = round((-var_b) / (2 * var_a),2)
vertex_y = round(var_a * vertex_x**2 + var_b * vertex_x + var_c, 2)
print("The vertex is {}, {}.".format(vertex_x, vertex_y))
if var_a >= 0:
    print("The vertex is a minimum value.")
else:
    print("The vertex is a maximum value.")
print("The axis of symmetry is x = {}".format(vertex_x))
