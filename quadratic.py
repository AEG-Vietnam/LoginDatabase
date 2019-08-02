########################################################################################################################
# File name: quadratic.py
#
# Author: Graeme Melrose
#
# Description: This function inputs a quadratic polynomial from the user and returns the solutions.
########################################################################################################################


def input_value():
    print("This program can solve ANY quadratic equation!!")
    print("Please enter a, b, and c for the equation in the form: a*x^2 + b*x + c = 0")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    return a, b, c


def solves_quadratic(a, b, c):
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)

    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)

    delta = (b ** 2 - 4 * a * c)

    return x1, x2, delta


A, B, C = input_value()

A = float(A)
B = float(B)
C = float(C)

answer1, answer2, d = solves_quadratic(A, B, C)

if d > 0:
    print('first solution is', answer1, '\nsecond solution is', answer2)
elif d == 0:
    print('there is only one solution:', answer1)
else:
    print('COMPLEX SOLUTIONS!!!!\nfirst solution is', answer1, '\nsecond solution is', answer2)
a = 1
b = 2
print(a, ' + ', b, 'i', sep='')
print(a, ' - ', b, 'i', sep='')
