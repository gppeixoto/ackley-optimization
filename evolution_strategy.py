import numpy as np
from numpy.random import randn
from utils import Ackley

class EvolutionStrategy:
    def __init__(self, generations=5000, population_size=1, mutation_step=0.1, adjust_mutation_constant=0.8):
        self.generations = generations
        self.population_size = population_size
        self.f_ackley = Ackley().f_x
        self.cromossome = None
        self.mutation_step = mutation_step
        self.adjust_mutation_constant = adjust_mutation_constant
        self.success_rate = .2
        self.num_mutations = 0
        self.num_successful_mutations = 0
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

    def get_success_probability(self):
        return self.num_successful_mutations / float(self.num_mutations)

    """
    Fitness function
    """
    def fitness(self, cromossome):
        return -1.*abs(self.f_ackley(cromossome))

    def adjust_mutation_step(self):
        ps = self.get_success_probability()
        if self.verbose == 1:
            print "ps: %.4f" % ps
        if ps > self.success_rate:
            self.mutation_step /= self.adjust_mutation_constant
        elif ps < self.success_rate:
            self.mutation_step *= self.adjust_mutation_constant
        if self.verbose == 1:
            print "mutation_step: %.4f" % self.mutation_step

    def apply_mutation(self):
        cromossome_prime = self.cromossome + self.get_mutation_vector()
        self.num_mutations += 1
        if self.fitness(self.cromossome) < self.fitness(cromossome_prime):
            self.cromossome = cromossome_prime
            self.num_successful_mutations += 1
        self.adjust_mutation_step()

    def run(self, verbose=0):
        self.verbose = verbose
        self.init_cromossome()
        gen = 0
        history = [(self.cromossome, self.f_ackley(self.cromossome))]
        if self.verbose == 1:
            print "gen: %d" % gen
            self.print_cromossome()
            print "Ackley(x): %.5f" % self.f_ackley(self.cromossome)
        while gen < self.generations:
            gen += 1
            self.apply_mutation()
            if self.verbose == 1:
                print "gen: %d" % gen
                self.print_cromossome()
                print "Ackley(x): %.5f" % self.f_ackley(self.cromossome)
            history.append((self.cromossome, self.f_ackley(self.cromossome)))
        return history

# es = EvolutionStrategy()
# es.run(verbose = 1)