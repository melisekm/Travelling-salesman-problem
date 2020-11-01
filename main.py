import tabu_search
from genetic_algorithm import GeneticAlgorithm

from utils import parse_input, print_riesenie

genetic_algorithm_args = [
    50,  # Velkost Generacie
    32,  # Max pocet Krizeni
    14,  # Max pocet Mutacii
    4,  # Max nahodnych chromozomov v generacii
    20,  # Pravdepodobnost mutacie v %
    1,  # Metoda vyberu rodicov, 1 - Ruleta, 2 - TODO
    1000,  # Max pocet iteracii
]

tabu_search_args = [
    500,  # Max velkost tabulky
    1000,  # Max pocet iteracii
]

if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    riesenie_genetic = GeneticAlgorithm(cities, genetic_algorithm_args)
    # riesenie_tabu = tabu_search.run(cities, 500) # TODO Refactor

    # print_riesenie(riesenie_tabu) #TODO
    print_riesenie(riesenie_genetic)  # print info
