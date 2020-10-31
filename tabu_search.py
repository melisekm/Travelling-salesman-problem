import math
import random
import timeit
import sys


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def fitness(stav):
    result = 0
    for i in range(len(stav) - 1):
        result += euclidian_d(stav[i], stav[i + 1])
    result += euclidian_d(stav[-1], stav[0])
    return result


def euclidian_d(city_A, city_B):
    result = math.sqrt((city_A.x - city_B.x) ** 2 + (city_A.y - city_B.y) ** 2)
    return int(round(result))


def vygenerujNasledovnikov(state):
    # """
    rand = random.randint(1, len(state) - 1)
    nasledovnici = []

    for i in range(1, len(state)):
        if i != rand:
            nasledovnik = state.copy()
            nasledovnik[i], nasledovnik[rand] = nasledovnik[rand], nasledovnik[i]
            nasledovnici.append(nasledovnik)

    return nasledovnici
    # """
    """
    neighborhood_size = 500
    neighbors = []

    for i in range(neighborhood_size):
        node1 = 0
        node2 = 0

        while node1 == node2:
            node1 = random.randint(1, len(state) - 1)
            node2 = random.randint(1, len(state) - 1)

        if node1 > node2:
            swap = node1
            node1 = node2
            node2 = swap

        tmp = state[node1:node2]
        tmp_state = state[:node1] + tmp[::-1] + state[node2:]
        neighbors.append(tmp_state)

    return neighbors
    """
    """
    nasledovnici = []

    for i in range(1, len(parent)):
        for j in range(i + 1, len(parent)):
            nasledovnik = parent.copy()
            nasledovnik[i], nasledovnik[j] = nasledovnik[j], nasledovnik[i]
            nasledovnici.append(nasledovnik)


    return nasledovnici
    """


def najdi_najlepsieho_kandidata(nasledovnici, tabu_list):
    kandidat = nasledovnici[0]

    for nasledovnik in nasledovnici:
        if nasledovnik not in tabu_list and fitness(nasledovnik) < fitness(kandidat):
            kandidat = nasledovnik

    return kandidat


def stop(start):
    return timeit.default_timer() - start > 60


def run(cities, maxTabuSize):
    maxTabuSize = 200
    stopAt = 1000
    nevylepsil = 0
    nahodny = [City(city[0], city[1]) for city in cities]
    globalne_max = nahodny
    najlepsi_kandidat = nahodny
    tabu_list = []
    tabu_list.append(nahodny)
    zmena = 0
    popol = 0
    iteracia = 0
    start = timeit.default_timer()
    sys.stdout = open("globalne_max.txt", "w")
    sys.stdout = open("best_candidate.txt", "w")
    while not stop(start):
        iteracia += 1
        # test = timeit.default_timer()
        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)
        # endtest = timeit.default_timer()
        # sys.stdout = sys.__stdout__
        # print(endtest - test)
        najlepsi_kandidat = najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

        najlepsi_kandidat_fitness = fitness(najlepsi_kandidat)
        globalne_max_fitness = fitness(globalne_max)

        sys.stdout = open("best_candidate.txt", "a")
        print(
            f"{round(timeit.default_timer() - start,2)} {najlepsi_kandidat_fitness} {len(tabu_list)} "
        )

        if najlepsi_kandidat_fitness < globalne_max_fitness:
            zmena += 1
            sys.stdout = open("globalne_max.txt", "a")
            globalne_max = najlepsi_kandidat
            print(f"{round(timeit.default_timer() - start,2)} {najlepsi_kandidat_fitness} ")
            nevylepsil = 0

        tabu_list.append(najlepsi_kandidat)
        if len(tabu_list) > maxTabuSize:
            popol += 1
            tabu_list.pop(0)

        if nevylepsil == stopAt:
            break

        nevylepsil += 1

    sys.stdout = sys.__stdout__
    print(iteracia, popol, zmena)
    return globalne_max
