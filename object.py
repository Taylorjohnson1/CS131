# Title: quadratic.py
# Date: 11/15/2020
# Author: Taylor Johnson
# Description: This program takes two different quadratic functions and outputs
# the y-intercept, roots and the sum of the quadratic function.

import math

class Quadratic:
    def __init__(self, a, b, c):
        '''Constructor function that initializes the attribute of the class.'''
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x):
        '''Given an x-value, evaluates the quadratic function to return the y-value'''
        one = (self.a * (x ** 2)) + (self.b * x) + self.c

        return one

    def roots(self):
        '''Computes the roots of the quadric function.'''
        root1 = (-self.b - math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a
        root2 = (-self.b + math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a

        return (root1, root2)

    def __str__(self):
        '''Return a string representation of the function.'''
        return ('%.2f(x)^2 + %.2f*2 + %.2f' % (self.a, self.b, self.c))


    def __add__(left, right):
        '''Add quadrtic functions together.'''
        # left and right are both objects of class Quadratic, similar to self.
        # Add the quadratic functions together and return the result.

        a = left.a + right.a
        b = left.b + right.b
        c = left.c + right.c

        return Quadratic(a, b, c)

def instructions():

    print()
    print("                       QUADRATIC")
    print("This program gathers two quadratic functions from the user.")
    print("It adds these functions together and finds the roots (x-intercepts)")
    print("and the y-intercept of the resulting function.")
    print()

def input_coeff():

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    return a, b, c

def main():

    instructions()

    should_quit = "n"

    while should_quit != "y":

        # Inputs
        print()
        print("Enter a quadratic function: f(x) = ax^2 + bx + c")
        a1, b1, c1 = input_coeff()

        print()
        print("Enter another quadratic function: g(x) = ax^2 + bx + c")
        a2, b2, c2 = input_coeff()
        print()

        # Calculations
        quadratic1 = Quadratic(a1, b1, c1)
        quadratic2 = Quadratic(a2, b2, c2)

        # The results of this program are all based on sum of the two quadratics.
        sum_quadratic = quadratic1 + quadratic2

        # Roots are the x_intercepts
        root1, root2 = sum_quadratic.roots()

        y_intercept = sum_quadratic.evaluate(0)

        # Outputs
        print()
        print("You entered the quadratic functions:")
        print("f(x) =", quadratic1)
        print("g(x) =", quadratic2)

        print()
        print("The sum of these functions is:")
        print("(f+g)(x) =",sum_quadratic)

        print()
        print("The roots of (f+g)(x) are: %.2f, %.2f" % (root1, root2))
        print("The y-intercept of (f+g)(x) is: %.2f" % y_intercept)

        print()
        should_quit = input("Would you like to quit? (y/n) ")

    print()
    print("Goodbye")
    print()

if __name__ == "__main__":
    main()
