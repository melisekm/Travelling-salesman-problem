from tabu_search import TabuSearch
from simulated_annealing import SimulatedAnnealing
from genetic_algorithm import GeneticAlgorithm
from utils import parse_input, print_riesenie
import tests

genetic_algorithm_args = [
    50,  # Velkost Generacie
    32,  # Max pocet Krizeni
    14,  # Max pocet Mutacii
    4,  # Max nahodnych chromozomov v generacii
    20,  # Pravdepodobnost mutacie v %
    3,  # hladanie vyberu rodicov, 1 - Ruleta, 2 - Rank Selection, 3 - Turnaj
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


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    print("Zvolte si metodu:")
    print("Geneticky algoritmus[GA]")
    print("Simulovane zihanie[SA]")
    print("Tabu search[TABU]")
    hladanie = input()
    if hladanie.lower() == "ga":
        # print("Zadajte metodu vyberu rodicov: ")
        # print("[Ruleta], [Rank], [Turnaj]")
        # metoda = input()

        riesenie_GA = GeneticAlgorithm(cities, genetic_algorithm_args)
        print_riesenie(riesenie_GA)
    elif hladanie.lower() == "sa":
        riesenie_SA = SimulatedAnnealing(cities, simulated_annealing_args)
        print_riesenie(riesenie_SA)
    elif hladanie.lower() == "tabu":
        riesenie_TABU = TabuSearch(cities, tabu_search_args)
        print_riesenie(riesenie_TABU)
    # tests.GA_testovanie(cities, genetic_algorithm_args)
