#   A program that computes the roots of a quadratic equation
#   Illustrates use of the math library
#   Note: This prgoram crashes if the equaution has no real roots.
#   import math makes the math library available

import math

def main():
    print("This program finds the real solutuions to a quadratic")
    print()

    a = eval(input("Please enter the coefficent a: "))
    b = eval(input("Please enter the coefficent b: "))
    c = eval(input("Please enter the coefficent c: "))

    discRoot = math.sqrt((b * b) - (4 * a * c))
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)

    print()
    print("The solutions are:", root1, root2)

main()
