# Discrete Structures (CSCI 220)
# Winter 2024
# Assignment 3: Basic Mathematical Structures
# Abul Hasan


import inspect
import pandas as pd
from itertools import product
import random
import numpy as np
from numpy import number
from itertools import chain, combinations

# [1] Define a function get_function_type(func, func_domain, func_co_domain)
# that receives a function "func" and two sets - domain and co_domain and determines
# whether the function passed in is "partial", "bijectve", "injective", or "surjective".
# First, compute func_range by evaluating the function for each value of the domain.

def get_function_type(func, func_domain, func_co_domain):
    is_total = True
    is_partial = True
    is_injective =True
    my_range = set()
    for element in func_domain:
        image = func(element)
        if image not in func_co_domain:
            is_total = False
        elif image in my_range:
            is_injective = False
        else:
            my_range.add(image)

    is_surjective = my_range == func_co_domain
    is_bijective = is_injective and is_surjective
    return f"is_total {is_total}, is_partial {is_partial}, is_injective {is_injective}, is_surjective {is_surjective}, is_bijective {is_bijective}"


def f_identity(n):
    return n


def f_predecessor(n):
    return n - 1


def f_successor(n):
    return n + 1


def f_square(n):
    return n * n


def q1():
    decimals = set([i for i in range(10)])
    for func in [f_identity, f_successor, f_predecessor, f_square]:
        print(func.__name__, get_function_type(func, func_domain=decimals, func_co_domain=decimals))


# [2] Define functions that compute the following set operations. The first five functions are binary
# and should accept two arguments each, while the last function is unary and should accept only one argument.
# You may use built-in functions to your language or implement them yourself.
# set_union(set1, set2) : X ∪ Y
# set_intersection(set1, set2): X ∩ Y
# set_difference(set1, set2): X − Y
# set_symmetric_difference(set1, set2):  X ∆  Y
# set_cartesian_product(set1, set2): X x Y
# set_power_set(set1):  P(X)
# For example, if your sets are
# X = {"a", "ab", "abc", "abcd"}
# Y = {"a", "bb", "ccc", "dddd"}

def set_union(set1, set2):
    set3 = set1
    for element in set2:
        set3.add(element)
    return set3


def set_intersection(set1, set2):
    set3 = set()
    for element in set2:
        if element in set1:
            set3.add(element)
    return set3


def set_difference(set1, set2):
    set3 = set1
    for element in set2:
        if element in set1:
            set3.remove(element)
    return set3


def set_symmetric_difference(set1, set2):
    return set_difference(set_union(set1, set2), set_intersection(set1, set2))


def set_cartesian_product(set1, set2):
    set3 = set()
    for element1 in set1:
        for element2 in set2:
            set3.add((element1, element2))
    return set3


def set_power_set(set1):
    s = list(set1)
    return str(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


def q2():
    X = {"a", "ab", "abc", "abcd"}
    Y = {"a", "bb", "ccc", "dddd"}
    print("Union", set_union(X, Y))
    print("Intersection", set_intersection(X, Y))
    print("Difference", set_difference(X, Y))
    print("Symmetric Difference", set_symmetric_difference(X, Y))
    print("Cartesian Product", set_cartesian_product(X, Y))
    print("Power Set", set_power_set(X))
    print("Power Set", set_power_set(Y))


# [3] Consider the following sums of series:
# counting(n) = 1 + 2 + … + n
# squares(n) = 1^2 + 2^2 + 3^2 + … + n^2
# cubes(n) = 1^3 + 2^3 + 3^3 + … + n^3
# geomteric_series(a, r, n) = a + ar + ar^2 + … + ar^n
# arithemetic_series(n, a, d) = a + ad + 2ad + … + nad
# [a] Write functions to compute each sum by looping over the terms
# [b] Write functions to compute each term by using a closed-form formula available in slides or online
# [c] Compare the results (since there may be roundoff error, do not look for equality but rather a difference less than 1)
def q3():
    n = 10
    a = 5
    r = 6
    d = 4
    print("Sum Counting Numbers: ", sum_counting_formula(n), sum_counting_loop(n))
    print("Sum Squares: ", sum_squares_formula(n), sum_squares_loop(n))
    print("Sum Cubes: ", sum_cubes_formula(n), sum_cubes_loop(n))
    print("Sum Geometric: ", sum_geometric_formula(n, a, r), sum_geometric_loop(n, a, r))
    print("Sum Arithmetic: ", sum_arithmetic_formula(n, a, d), sum_arithmetic_loop(n, a, d))


def sum_counting_loop(n):
    return sum([i for i in range(1, n + 1)])


def sum_counting_formula(n):
    return (n * (n + 1)) / 2


def sum_squares_loop(n):
    return sum([i ** 2 for i in range(1, n + 1)])


def sum_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum_cubes_loop(n):
    return sum([i ** 3 for i in range(1, n + 1)])


def sum_cubes_formula(n):
    return (n * (n + 1) / 2) ** 2


def sum_geometric_loop(n, a, r):
    return sum([a * r ** i for i in range(0, n + 1)])


def sum_geometric_formula(n, a, r):
    return a * ((r ** (n + 1) - 1) / (r - 1))


def sum_arithmetic_loop(n, a, d):
    return sum([a + d * i for i in range(0, n + 1)])


def sum_arithmetic_formula(n, a, d):
    return a * (n + 1) + d * n * (n + 1)/2


# [4] Consider a pair of matrices
#
# [a] Code the generation of random n x n integer matrices and call it twice.
# [b] Code the sum of the matrices using loops, list comprehension,  and numpy.matrix.sum(), and compare the results
# [c] Code the product of the matrices using loops, list comprehension,  and numpy.multiply(), and compare the results.
def random_matrix(n):
    return [[random.randint(1, 10) for i in range(n)] for j in range(n)]


def sum_matrices(m1, m2):
    n = len(m1)
    m3 = [[0] * n for j in range(n)]
    for i in range(n):
        for j in range(n):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3


def sum_matrices_list_comp(m1, m2):
    n = len(m1)
    m3 = [[m1[i][j] + m2[i][j] for i in range(n)] for j in range(n)]
    return m3


def mult_matrices_loop(m1, m2):
    n = len(m1)
    m3 = [[0] * n for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3


def mult_matrices_list_comp(m1, m2):
    n = len(m1)
    m3 = [[sum([m1[i][k] * m2[i][j] for k in range(n)]) for j in range(n)] for i in range(n)]
    return m3


def print_matrix(m):
    print(np.array(m))
    print()


def q4():
    m1 = random_matrix(5)
    m2 = random_matrix(5)
    sum1 = sum_matrices(m1, m2)
    sum2 = sum_matrices_list_comp(m1, m2)
    print_matrix(sum1)
    print_matrix(sum2)

    mult1 = mult_matrices_loop(m1, m2)
    mult2 = mult_matrices_list_comp(m1, m2)
    print_matrix(mult1)
    print_matrix(mult2)


# [5] Define a function generate_binary_number(binary_numbers) that takes a list of the string representation of some fractional binary numbers in the range [0,1) and uses Cantor's diagonalization argument to find a number not already in that list. Be mindful of the case where there are more elements in the list than digits in each number, and assume implicit trailing zeros as needed.
# 0.010011 # 0 x 1/2 + 1 x 1/4 + 0 x 1/8 + 0 x 1/16 + 1 x 1/32 + 1 x 1/64
# 0.101010 # 1 x 1/2 + 0 x 1/4 + 1 x 1/8 + 0 x 1/16 + 1 x 1/32 + 0 x 1/64
# 0.111000
# 0.000111
# 0.111111
# 0.111000
def generate_binary_number(numbers):
    return "0." + "".join(["1" if numbers[i][i + 2] == "0" else "0" for i in range(len(numbers))])  # i+2 skips "0."


def convert_to_decimal(number):
    return sum([int(number[i]) / 2 ** (i - 1) for i in range(2, len(number))])


def q5():
    numbers = ["0.010011", "0.101010", "0.111000", "0.000111", "0.111111", "0.111000"]
    for number in numbers:
        print("Old number:", number, convert_to_decimal(number))
    number = generate_binary_number(numbers)
    print("New number:", number, convert_to_decimal(number))


# [6] Define a  function that derives a closed-form formula for the summation s(n, p) = 1p + 2p + … + np,
# using the method demonstrated in class, i.e. derive the coefficients of a polynomial of degree p+1 that gives s(n, p)
# Follow these steps for a given p. (In class, we did it for p = 2)
# Define a Python function s(n, p) that uses a loop to find s(n, p) = 1p + 2p + … + np
# Generate the "vector" (one-dimensional matrix) b by finding for each row j = 0, 1, 2, …, p, the value of s(j, p)
# Generate the "matrix" A by finding for each row j = 0, 1, 2, …, p, the values jp+1, jp, jp-1,..., j0.
# Solve the system of linear equations Ax = b. The solution vector x will be the coefficients of the polynomial.
# Test the polynomial to see that it matches s(n, p)
def q6():
    pass


def main():
    questions = [q1, q2, q3, q4, q5, q6]
    for q in questions:
        print("question", q.__name__)
        q()
        print()


if __name__ == "__main__":
    main()
