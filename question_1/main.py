import equations
import time
import numpy as np
import cvxpy as cp
from plot import plot_times

TEST_SIZE = 150

def time_numpy(max_size):
    times = []
    for n in range(1, max_size+1):
        (lhs, rhs) = equations.numpy_linear_eq(n, n, 1, 1000)
        t1 = time.time()
        np.linalg.solve(lhs, rhs)
        diff = time.time() - t1
        times.append(diff)
    return times

def time_cvxpy(max_size):
    times = []
    for n in range(1, max_size+1):
        (A, b) = equations.numpy_linear_eq(n, n, 1, 1000)
        x = cp.Variable(n)
        objective = cp.Minimize(cp.)
        prob = cp.Problem(objective, [A @ x == b])
        t1 = time.time()
        prob.solve()
        diff = time.time() - t1
        times.append(diff)
    return times

times = time_numpy(TEST_SIZE)
input_sizes = [i for i in range(1, TEST_SIZE+1)]
plot_times(input_sizes, times)


times = time_cvxpy(TEST_SIZE)
input_sizes = [i for i in range(1, TEST_SIZE+1)]
plot_times(input_sizes, times)