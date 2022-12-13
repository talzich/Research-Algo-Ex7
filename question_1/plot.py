import numpy as np
import matplotlib.pyplot as plt


def plot_times(input_sizes, times):
    x = np.array(input_sizes)
    y_np = np.array(times['np'])
    y_cp = np.array(times['cp'])
    
    _, ax = plt.subplots()
    ax.plot(x, y_np, color='r', label='numpy')
    ax.plot(x, y_cp, color='b', label='cvxpy')
    ax.set(xlabel='input size', ylabel='time (s)',
       title='Run Time')
    ax.grid()
    ax.legend()
    plt.show()