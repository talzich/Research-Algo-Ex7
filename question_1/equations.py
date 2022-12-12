import numpy as np
import cvxpy
from cvxpy import log

def numpy_linear_eq(rows, cols, low_end, high_end):
    """ Creates a random linear equation using numpy

    This function takes number of rows and rows and cols for the the linear equation
    and the lower and higher ends of the random function and produces a matrix describing the linear
    equation.
    The function returns a pair with the left hand being the coefficients and the right hand side being the solutions
    """

    lhs = np.random.randint(low_end, high_end, size=(rows, cols))
    rhs = np.random.randint(low_end, high_end, size=(rows, 1))
    return (lhs, rhs)


def cvxpy_linear_eq(rows, cols, low_end, high_end):
    """ Creates a random linear equation using cvxpy

    This function takes number of rows and rows and cols for the the linear equation
    and the lower and higher ends of the random function and produces a matrix describing the linear
    equation.
    The function returns a pair with the left hand being the coefficients and the right hand side being the solutions
    """
    print(cvxpy.Variable((rows, cols)))
    