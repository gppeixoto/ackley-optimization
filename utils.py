import numpy as np

class Ackley:
    def __init__(self, N=30):
        self.N = N
        self.c1 = 20
        self.c2 = 0.2
        self.c3 = 2*np.pi

    def f_x(self, x):
        part1 = -1. * self.c1 * np.exp(
            -1. * self.c2 * np.sqrt((1./self.N) * sum(map(lambda nb: nb**2, x)))
            )
        part2 = -1. * np.exp(
            (1./self.N) * \
            sum(map(lambda nb: np.cos(self.c3 * nb), x))
            )
        return part1 + part2 + self.c1 + np.exp(1)
