from genetic_algorithm import GeneticAlgorithm
from utils import print_riesenie


def GA_testovanie(cities, genetic_algorithm_args):
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
