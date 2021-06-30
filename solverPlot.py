import numpy as np
import casadi as ca
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SolverPlot(object):

    """Plotting robot trajectories for various robots"""

    def __init__(self, solverTimes, n, m, axs=None):
        self._solverTimes = solverTimes
        if axs is None:
            self._fig, axs = plt.subplots(n, m, figsize=(m*4, n*4))
            self._axs = axs.flatten()
        else:
            self._axs = axs


    def plot(self):
        for i, s in enumerate(self._solverTimes):
            self._axs[i].hist(s, bins=100)

    def show(self):
        plt.show()

