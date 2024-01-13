# Queens College
# Discrete Structures (CSCI 220)
# Winter 2024
# Assignment 9:
# Abul Hasan
# Collaborated with Class


import math
import random
import texttable
import numpy as np
import Assignment8 as as8




# [1] Define a function to parse a linear homogeneous recurrence and extract both its initial conditions  and coefficients
def get_sides(eqn):
    parts = eqn.split("=")
    return parts[0].strip(), parts[1].strip()


def get_rhs(eqn):
    parts = eqn.split("=")
    return get_sides()[1]


def parse_recurrence(recurrence):
    var = recurrence.strip
    parts = recurrence.split(",")
    f_0 = float(get_rhs(parts[0]))
    f_1 = float(get_rhs(parts[1]))
    f_n = get_rhs(parts[2])
    idx1 = f_n.find(var)
    temp1 = f_n[:idx1].strip()
    c1 = 1 if temp1 == "" else float(temp1)
    idx2 = f_n.find(")")
    idx3 = f_n.find(var, idx2 + 1)
    temp2 = f_n[idx2 + 1:idx3].replace(" ", "").strip()
    c2 = 1 if temp2 == "+" or temp2 == "-" else float(temp2)
    return var, f_0, f_1, c1, c2


# [2] Define a function to reconstruct the recurrence from the parameters and print the recurrence in standard form.
def reconstruct_recurrence(var, c1, c2, a1, a0):
    recurrence = f"{var}(0) = {a0}, {var}(1) = {a1}, {var}(n) = {c1}{var(n-1)} + {c2} {var}(n-2)"
    return recurrence

# [3] Define a function to determine and print the characteristic equation for the recurrence
def solve_characteristic_equations(c1,c0):
    a = 1
    b = -1 * c1
    c = -1 * c0
    temp = math.sqrt(b**2 - 4*a*c)
    r1 = ((-1 * b) + temp) / (2*a)
    r2 = ((-1 * b) - temp) / (2*a)
    return characteristic_equation, r1 and r2
# [4[ Define a function to find the root(s) of the characteristic equation
 
# [5] Define a function to determine the coefficients of those roots in the solution. Make sure to handle both the case of distinct and duplicate roots. 

# [6] Define a function to display the closed-form formula using the results of the previous tasks

# [7] For several different linear homogeneous recurrences,
# print the recurrence
# print the context in which it arises (e.g. slide or website)
# solve the recurrence
# evaluate the recurrence (use code from previous assignment and compare  with closed form)
# plot the value

# [8] Collect the output for all the functions and present it in a table,
# Use this code as a starting point for some of the tasks above. 
def solve_recurrence(desc, c1, c0, a0, a1):
    print(desc)
    recurrence = "a(n) = " + str(c1) + "*a(n-1) + " + str(c0) + "*a(n-2)"
    print("The recurrence is", recurrence)
    characteristic_equation = "r^2 - " + ("" if c1 == 1 else str(c1)) + "r - " + str(c0)
    print("characteristic equation is", characteristic_equation)
    a = 1
    b = -1 * c1
    c = -1 * c0
    temp = math.sqrt(b**2 - 4*a*c)
    r1 = ((-1 * b) + temp) / (2*a)
    r2 = ((-1 * b) - temp) / (2*a)
    print("The roots are ", r1, r2)
    distinct = r1 != r2
    A = np.array([[r1 ** 0, (0 if not distinct else 1) * r2 ** 0], [r1 ** 1, (1 if not distinct else 1) * r2 ** 1]])
    B = np.array([a0, a1])
    X = np.linalg.solve(A, B)
    print("The coefficients are", X[0], X[1])
    formula = "a(n) = " + str(X[0]) + "*" + str(r1) + "^n" + " + " + str(X[1]) + "*" + ("n*" if not distinct else "") + str(r2) + "^n" 
    print("The closed-form formulas is", formula)
    a2_recurrence = c1*a1 + c0*a0
    a2_formula = X[0]*r1**2 + X[1]*(2 if not distinct else 1)*r2**2
    print("a2_recurrence", a2_recurrence)
    print("a2_formula", a2_formula)
    print()




def main():
    recurrence = "f(0)=0, f(1) = 1, f(n)= f(n-1)+f(n-2)"
    var, a0, a1, c1, c2 = parse_recurrence(recurrence)
    new_recurrence = reconstruct_recurrence(var, a0, a1, c1,c2)
    characteristic_equation, r1, r2 = solve_characteristic_equations(c1,c2)
    print("old recurrence ", recurrence)
    print("new recurrence ", new_recurrence)
    print("characteristic equation is ", characteristic_equation)
    print("the roots are", r1, r2)



if __name__ == '__main__':
    main()