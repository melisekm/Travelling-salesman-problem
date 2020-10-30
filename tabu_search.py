import math
import random
import timeit


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        result = 0
        for i in range(len(self) - 1):
            result += euclidian_d(self[i], self[i + 1])
        result += euclidian_d(self[-1], self[0])
        return result


def euclidian_d(city_A, city_B):
    return math.sqrt((city_A.x - city_B.x) ** 2 + (city_A.y - city_B.y) ** 2)


def vygenerujNasledovnikov(parent):
    nasledovnici = []

    for i in range(1, len(parent)):
        for j in range(i + 1, len(parent)):
            nasledovnik = parent.copy()
            nasledovnik[i], nasledovnik[j] = nasledovnik[j], nasledovnik[i]

            nasledovnici.append(Node(nasledovnik))

    return nasledovnici


def najdi_najlepsieho_kandidata(nasledovnici, tabu_list):
    kandidat = nasledovnici[0]

    for nasledovnik in nasledovnici:
        if not nasledovnik in tabu_list and nasledovnik.fitness < kandidat.fitness:
            kandidat = nasledovnik

    return kandidat


def stop(start):
    return timeit.default_timer() - start > 0.5


def run(cities, maxTabuSize):
    maxTabuSize = 100
    nahodny = Node([City(city[0], city[1]) for city in cities])
    globalne_max = nahodny
    najlepsi_kandidat = nahodny
    tabu_list = []
    tabu_list.append(nahodny)
    start = timeit.default_timer()
    while not stop(start):
        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)
        najlepsi_kandidat = najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

        if najlepsi_kandidat.fitness < globalne_max.fitness:
            globalne_max = najlepsi_kandidat

        tabu_list.append(najlepsi_kandidat)
        if len(tabu_list) > maxTabuSize:
            tabu_list.pop()

    return globalne_max
