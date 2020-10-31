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
    rand = random.randint(1, len(state) - 1)
    nasledovnici = []

    for i in range(1, len(state)):
        if i != rand:
            nasledovnik = state.copy()
            nasledovnik[i], nasledovnik[rand] = nasledovnik[rand], nasledovnik[i]
            nasledovnici.append(nasledovnik)

    return nasledovnici


def najdi_najlepsieho_kandidata(nasledovnici, tabu_list):
    kandidat = nasledovnici[0]

    for nasledovnik in nasledovnici:
        if nasledovnik not in tabu_list and fitness(nasledovnik) < fitness(kandidat):
            kandidat = nasledovnik

    return kandidat


def stop(start):
    return timeit.default_timer() - start > 30


def run(cities, maxTabuSize):
    maxTabuSize = 500
    stopAt = 2000
    nevylepsil = 0
    nahodny = [City(city[0], city[1]) for city in cities]
    globalne_max = nahodny
    najlepsi_kandidat = nahodny
    tabu_list = []
    tabu_list.append(nahodny)
    start = timeit.default_timer()
    sys.stdout = open("globalne_max.txt", "w")
    sys.stdout = open("best_candidate.txt", "w")
    while not stop(start) and nevylepsil != stopAt:

        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)
        najlepsi_kandidat = najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

        najlepsi_kandidat_fitness = fitness(najlepsi_kandidat)
        globalne_max_fitness = fitness(globalne_max)

        sys.stdout = open("best_candidate.txt", "a")
        print(
            f"{round(timeit.default_timer() - start,2)} {najlepsi_kandidat_fitness} {len(tabu_list)}"
        )

        if najlepsi_kandidat_fitness < globalne_max_fitness:
            sys.stdout = open("globalne_max.txt", "a")
            globalne_max = najlepsi_kandidat
            print(f"{round(timeit.default_timer() - start,2)} {najlepsi_kandidat_fitness} ")
            nevylepsil = 0

        tabu_list.append(najlepsi_kandidat)
        if len(tabu_list) > maxTabuSize:
            tabu_list.pop(0)

        nevylepsil += 1

    sys.stdout = sys.__stdout__
    return globalne_max
