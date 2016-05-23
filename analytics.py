from evolution_strategy import TwoMemberEvolutionStrategy as ES
from alternate_evolution_strategy import EvolutionStrategy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# generations=200000, population_size=1, mutation_step=10, adjust_mutation_constant=0.8

def generate_configurations():
    gens = [5000, 10000, 15000]
    mutation_steps = [1, 5, 10]
    adjust_mutation_constants = [.8, .85, .9]
    configs = []
    for gen in gens:
        for mutation_step in mutation_steps:
            for constant in adjust_mutation_constants:
                config = {
                    "generations": gen,
                    "mutation_step": mutation_step,
                    "adjust_mutation_constant": constant
                }
                configs.append(config)
    return configs

def get_evolution_configurations():
    # gens = [5000, 10000, 15000]
    recombination_strategies = ["discrete_recombination", "intermediate_recombine"]
    learning_rates = [(1./np.sqrt(30)), np.sqrt(30)]
    pop_children = [(30,200), (60,400)]
    configs = []
    for learning_rate in learning_rates:
        for recombination_strategy in recombination_strategies:
            for pc in pop_children:
                config = {
                    "recombination_strategy": recombination_strategy,
                    "learning_rate": learning_rate,
                    "population_size": pc[0],
                    "num_children": pc[1]
                }
                configs.append(config)
    return configs

def one_plus_one_es_analytics():
    configs = generate_configurations()
    df_rows = []
    for config in configs:
        print config
        es = ES(generations=config["generations"],
                mutation_step=config["mutation_step"],
                adjust_mutation_constant=config["adjust_mutation_constant"])
        history, elapsed_time = es.run()
        fitness_history = pd.Series(t[1] for t in history)
        best = fitness_history.min()
        mean = fitness_history.mean()
        std = fitness_history.std()
        row = (config["generations"], config["mutation_step"],
                       config["adjust_mutation_constant"], best, mean,
                       std, elapsed_time)
        df_rows.append(row)
        print row
    df = pd.DataFrame(df_rows, columns=["generations", "mutation_step", \
                                "adjust_mutation_constant", "best_fitness", \
                                "mean_fitness", "std_fitness", "time_elapsed"])
    with open("table.html", "w") as outfile:
        outfile.write(df.to_html())

def evolution_strategy_analytics(N=10):
    configs = get_evolution_configurations()
    df_rows = []
    for config in configs:
        rows = []
        for i in xrange(N):
            es = EvolutionStrategy(
                recombination_strategy=config["recombination_strategy"],
                population_size=config["population_size"],
                learning_rate=config["learning_rate"],
                num_children=config["num_children"]
                )
            history, elapsed_time, generations = es.run(verbose=1)
            fitness_history = pd.Series(t[1] for t in history)k
            best = fitness_history.min()
            mean = fitness_history.mean()
            std = fitness_history.std()
            row = (best, mean, std, elapsed_time, generations)
            rows.append(row)
        df = pd.DataFrame(rows, columns=["best", "mean", "std", "elapsed_time", "generations"])


if __name__ == "__main__":
    one_plus_one_es_analytics()
