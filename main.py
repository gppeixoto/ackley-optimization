import evolution_strategy as tmes
import alternate_evolution_strategy as aes

def main():
    es = aes.EvolutionStrategy()
    es.run(verbose = 1)

if __name__ == "__main__":
    main()