from concurrent.futures import ProcessPoolExecutor
from genetic_algorithm import GeneticAlgorithm
from simulated_annealing import SimulatedAnnealing
from tabu_search import TabuSearch
from utils import load_input, print_riesenie

genetic_algorithm_args = [
    50,  # Velkost Generacie
    32,  # Max pocet Krizeni
    14,  # Max pocet Mutacii
    4,  # Max nahodnych chromozomov v generacii
    60,  # Pravdepodobnost mutacie v %
    1,  # hladanie vyberu rodicov, 1 - Ruleta, 2 - Rank Selection, 3 - Turnaj
    -1,  # Max pocet iteracii
    15,  # Max dlzka trvania v sek
]

tabu_search_args = [
    500,  # Max velkost tabu listu
    -1,  # Max pocet iteracii
    15,  # Max dlzka trvania v sek
]

simulated_annealing_args = [
    0.00005,  # Rychlost ochladenia 1 - x
    1e-6,  # Pociatocna teplota je sqrt(pocet_miest)
    1e-8,  # Min teplota
    60,  # Max dlzka trvania v sek
]


if __name__ == "__main__":
    print("Nastavte parametre algoritmov v programe.")
    while True:
        vstup, cities, metoda = load_input()
        if cities is None:
            print("Zly vstup :)")
            continue

        if metoda.lower() == "vsetky":
            with ProcessPoolExecutor(max_workers=3) as executor:
                riesenie_GA = executor.submit(GeneticAlgorithm, cities, genetic_algorithm_args)
                riesenie_SA = executor.submit(SimulatedAnnealing, cities, simulated_annealing_args)
                riesenie_TABU = executor.submit(TabuSearch, cities, tabu_search_args)
            print_riesenie(riesenie_GA.result(), vstup)
            print_riesenie(riesenie_SA.result(), vstup)
            print_riesenie(riesenie_TABU.result(), vstup)

        elif metoda.lower() == "ga":
            riesenie_GA = GeneticAlgorithm(cities, genetic_algorithm_args)
            print_riesenie(riesenie_GA, vstup)
        elif metoda.lower() == "sa":
            riesenie_SA = SimulatedAnnealing(cities, simulated_annealing_args)
            print_riesenie(riesenie_SA, vstup)
        elif metoda.lower() == "tabu":
            riesenie_TABU = TabuSearch(cities, tabu_search_args)
            print_riesenie(riesenie_TABU, vstup)
