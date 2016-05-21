import numpy as np

class Ackley:
    def __init__(self, N=30, C1=20, C2=.2, C3=2*np.pi):
        self.N = N
        self.c1 = C1
        self.c2 = C2
        self.c3 = C3

    def f_x(self, x):
        part1 = -1. * self.c1 * np.exp(
            -1. * self.c2 * np.sqrt((1./self.N) * sum(map(lambda nb: nb**2, x)))
            )
        part2 = -1. * np.exp(
            (1./self.N) * \
            sum(map(lambda nb: np.cos(self.c3 * nb), x))
            )
        return part1 + part2 + self.c1 + np.exp(1)
