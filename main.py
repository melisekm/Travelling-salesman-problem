from genetic_algorithm import GeneticAlgorithm
from simulated_annealing import SimulatedAnnealing
from tabu_search import TabuSearch
from utils import parse_input, print_riesenie
from concurrent.futures import ProcessPoolExecutor
import timeit

genetic_algorithm_args = [
    50,  # Velkost Generacie
    32,  # Max pocet Krizeni
    14,  # Max pocet Mutacii
    4,  # Max nahodnych chromozomov v generacii
    20,  # Pravdepodobnost mutacie v %
    2,  # hladanie vyberu rodicov, 1 - Ruleta, 2 - Rank Selection, 3 - Turnaj
    5000,  # Max pocet iteracii
    13,  # Max dlzka trvania v sek
]

tabu_search_args = [
    500,  # Max velkost tabu listu
    2000,  # Max pocet iteracii
    13,  # Max dlzka trvania v sek
]

simulated_annealing_args = [
    0.00005,  # Rychlost ochladenia 1 - x
    1e-8,  # Min teplota
    # Pociatocna teplota je sqrt(pocet_miest)
    30,  # Max dlzka trvania v sek
]


def ga_fun(cities, args):
    obj = GeneticAlgorithm(cities, args)
    print_riesenie(obj)


def sa_fun(cities, args):
    obj = SimulatedAnnealing(cities, args)
    print_riesenie(obj)


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    """
    print("Zvolte si metodu:")
    print("Geneticky algoritmus[GA]")
    print("Simulovane zihanie[SA]")
    print("Tabu search[TABU]")
    """
    start = timeit.default_timer()

    with ProcessPoolExecutor(max_workers=3) as executor:
        riesenie_GA = executor.submit(GeneticAlgorithm, cities, genetic_algorithm_args)
        riesenie_SA = executor.submit(SimulatedAnnealing, cities, simulated_annealing_args)
        riesenie_TABU = TabuSearch(cities, tabu_search_args)
        print_riesenie(riesenie_GA.result())
        print_riesenie(riesenie_SA.result())
        print_riesenie(riesenie_TABU)

    # print("som vonku")
    """
    # hladanie = input()
    # if hladanie.lower() == "ga":
    riesenie_GA = GeneticAlgorithm(cities, genetic_algorithm_args)
    print_riesenie(riesenie_GA)
    # elif hladanie.lower() == "sa":
    riesenie_SA = SimulatedAnnealing(cities, simulated_annealing_args)
    print_riesenie(riesenie_SA)
    # elif hladanie.lower() == "tabu":
    # riesenie_TABU = TabuSearch(cities, tabu_search_args)
    # print_riesenie(riesenie_TABU)
    """
    end = timeit.default_timer()
    print(end - start)