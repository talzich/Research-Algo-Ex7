import numpy as np
import matplotlib.pyplot as plt


def plot_times(input_sizes, times):
    x = np.array(input_sizes)
    y = np.array(times)
    
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='input size', ylabel='time (s)',
       title='Run Time')
    ax.grid()

    plt.show()