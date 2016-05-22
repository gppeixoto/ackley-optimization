from evolution_strategy import TwoMemberEvolutionStrategy as ES
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

def generate_statistics():
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

if __name__ == "__main__":
    generate_statistics()
