import tabu_search
from simulated_annealing import SimulatedAnnealing
from genetic_algorithm import GeneticAlgorithm
from utils import parse_input, print_riesenie

genetic_algorithm_args = [
    50,  # Velkost Generacie
    32,  # Max pocet Krizeni
    14,  # Max pocet Mutacii
    4,  # Max nahodnych chromozomov v generacii
    20,  # Pravdepodobnost mutacie v %
    3,  # Metoda vyberu rodicov, 1 - Ruleta, 2 - Rank Selection, 3 - Turnaj
    1000,  # Max pocet iteracii
    30,  # Max dlzka trvania v sek
]

tabu_search_args = [
    500,  # Max velkost tabu listu
    200,  # Max pocet iteracii
    30,  # Max dlzka trvania v sek
]

simulated_annealing_args = [
    0.0005,  # Rychlost ochladenia 1 - x
    1e-8,  # Min teplota
    # Pociatocna teplota je sqrt(pocet_miest)
    30,  # Max dlzka trvania v sek
]


def GA_testovanie():
    # default_args_GA = genetic_algorithm_args.copy()
    """
    tmp_args = default_args_GA.copy()
    genetic_algorithm_args[5] = 3

    for i in range(4):
        tmp_args[i] *= 5  # nastavenia
    riesenie_genetic = GeneticAlgorithm(cities, tmp_args)
    print_riesenie(riesenie_genetic)  # print info

    """
    for i in range(1, 4):
        genetic_algorithm_args[5] = i
        tmp_args = genetic_algorithm_args.copy()

        riesenie_genetic = GeneticAlgorithm(cities, genetic_algorithm_args)
        print_riesenie(riesenie_genetic)  # print info

        for i in range(4):
            tmp_args[i] *= 5

        riesenie_genetic = GeneticAlgorithm(cities, tmp_args)
        print_riesenie(riesenie_genetic)  # print info


if __name__ == "__main__":
    cities = parse_input("vstup.txt")

    riesenie_genetic = GeneticAlgorithm(cities, genetic_algorithm_args)
    print_riesenie(riesenie_genetic)  # print info

    # GA_testovanie()

    # riesenie_SA = SimulatedAnnealing(cities, simulated_annealing_args)
    # print_riesenie(riesenie_SA)

    # riesenie_tabu = tabu_search.run(cities, 200)  # TODO Refactor
    # print_riesenie(riesenie_tabu)  # TODO
