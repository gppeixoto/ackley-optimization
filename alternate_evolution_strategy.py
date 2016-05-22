import numpy as np
import random
import utils
from operator import itemgetter

class EvolutionStrategy:
    def __init__(self, generations=200000, population_size=30, num_children=200):
        self.generations = generations
        self.population_size = population_size
        self.num_children = num_children
        self.children = []
        self.dimensions = 30
        self.f_ackley = utils.Ackley().f_x
        self.population = []
        self.mutation_steps = [1.0] * self.num_children
        self.learning_rate = float(1) / np.sqrt(self.dimensions)
        self.verbose = 0
        self.delta = 1e-8

    def print_cromossome(self, cromossome):
        print '[' + ','.join(["%.2f" % nb for nb in cromossome]) + ']'

    """
    Init cromossomes with uniform distribution
    """
    def init_cromossome(self):
        return self.dimensions*np.random.random(30)-15

    def init_population(self):
        for i in xrange(self.population_size):
            self.population.append(self.init_cromossome())

    """
    Init mutation steps with lognormal distribution
    """        
    def adjust_mutation_steps(self):
        for i in xrange(self.num_children):
            new_step = self.mutation_steps[i] * np.exp(self.learning_rate * np.random.normal())
            self.mutation_steps[i] = new_step if new_step > self.delta else self.delta

    def get_mutation_vector(self, mutation_step):
        return np.random.normal(0, mutation_step, self.dimensions)

    """
    Fitness function
    """
    def fitness(self, cromossome):
        return self.f_ackley(cromossome)

    """
    Recombination: discrete recombination
    """
    def select_parents(self):
        parent_1 = random.choice(self.population)
        parent_2 = random.choice(self.population)
        return parent_1, parent_2

    def recombine(self, parent_1, parent_2):
        child = []
        for pair in zip(parent_1, parent_2):
            child.append(random.choice(pair))
        return child

    def get_next_generation(self):
        self.children = []
        for i in xrange(self.num_children):
            parent_1, parent_2 = self.select_parents()
            self.children.append(self.recombine(parent_1, parent_2))

    def apply_mutations(self):
        self.adjust_mutation_steps()
        for i in xrange(self.num_children):
            self.children[i] = utils.sum_vectors(self.children[i], self.get_mutation_vector(self.mutation_steps[i]))

    def selection(self):
        child_fit_pairs = [(child, self.fitness(child)) for child in self.children]
        ordered_children = sorted(child_fit_pairs, key=itemgetter(1))
        self.population = []
        for i in xrange(self.population_size):
            self.population.append(ordered_children[i][0])

    """
    Algorithm
    """

    def run(self, verbose=0):
        self.verbose = verbose
        self.init_population()
        gen = 0
        history = []
        while gen < self.generations:
            gen += 1
            self.get_next_generation()
            self.apply_mutations()
            self.selection()
            best_individual = self.population[0]
            if self.verbose == 1:
                print "gen: %d" % gen
                self.print_cromossome(best_individual)
                print "Ackley(x): %.15f" % self.f_ackley(best_individual)
            history.append((best_individual, self.f_ackley(best_individual)))
        return history