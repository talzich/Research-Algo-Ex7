import equations
import time
import numpy as np
from plot import plot_times

def time_numpy(max_size):
    times = []
    for n in range(1, max_size+1):
        (lhs, rhs) = equations.numpy_linear_eq(n, n, 1, 50)
        t1 = time.time()
        np.linalg.solve(lhs, rhs)
        diff = time.time() - t1
        times.append(diff)
    return times

times = time_numpy(700)
input_sizes = [i for i in range(1, 701)]
plot_times(input_sizes, times)