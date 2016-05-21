import numpy as np
from numpy.random import randn
from utils import Ackley

class EvolutionStrategy:
    def __init__(self, generations=50, population_size=1):
        self.generations = generations
        self.population_size = population_size
        self.f_ackley = Ackley().f_x
        self.cromossome = None
        self.mutation_step = .1
        self.adjust_mutation_constant = .8
        self.success_rate = .2
        self.verbose = 0

    def print_cromossome(self):
        print '[' + ','.join(["%.2f" % nb for nb in self.cromossome]) + ']'

    """
    Init cromossome with uniform distribution
    """
    def init_cromossome(self):
        self.cromossome = 30*np.random.random(30)-15

    def get_mutation_vector(self):
        return np.random.normal(0, self.mutation_step, 30)

    """
    Identity function
    """
    def fitness(self, nb):
        return -1.*abs(nb)

    def adjust_mutation_step(self, ps):
        if ps > self.success_rate:
            self.mutation_step /= self.adjust_mutation_constant
        elif ps < self.success_rate:
            self.mutation_step *= self.adjust_mutation_constant

    def apply_mutation(self):
        cromossome_prime = self.cromossome + self.get_mutation_vector()
        ps = 0
        for i, x_i_prime in enumerate(cromossome_prime):
            x_i = self.cromossome[i]
            if self.fitness(x_i_prime) < self.fitness(x_i):
                cromossome_prime[i] = x_i
                ps += 1
        ps /= (1. * cromossome_prime.size)
        self.adjust_mutation_step(ps)
        self.cromossome = cromossome_prime

    def run(self, verbose=0):
        self.verbose = verbose
        self.init_cromossome()
        gen = 0
        while gen < self.generations:
            self.apply_mutation()
            if self.verbose == 1:
                print "gen: %d" % gen
                self.print_cromossome()
            gen += 1
        # TODO: finish run implementation
