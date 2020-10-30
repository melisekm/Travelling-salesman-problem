import math
import random
import timeit


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


def vygenerujNasledovnikov(parent):
    nasledovnici = []

    for i in range(1, len(parent)):
        for j in range(i + 1, len(parent)):
            nasledovnik = parent.copy()
            nasledovnik[i], nasledovnik[j] = nasledovnik[j], nasledovnik[i]

            nasledovnici.append(nasledovnik)

    return nasledovnici


def najdi_najlepsieho_kandidata(nasledovnici, tabu_list):
    kandidat = nasledovnici[0]

    for nasledovnik in nasledovnici:
        if not nasledovnik in tabu_list and fitness(nasledovnik) < fitness(kandidat):
            kandidat = nasledovnik

    return kandidat


def stop(start):
    return timeit.default_timer() - start > 20


def run(cities, maxTabuSize):
    maxTabuSize = 100
    nahodny = [City(city[0], city[1]) for city in cities]
    globalne_max = nahodny
    najlepsi_kandidat = nahodny
    tabu_list = []
    tabu_list.append(nahodny)
    zmena = 0
    popol = 0
    iteracia = 0
    start = timeit.default_timer()
    while not stop(start):
        iteracia += 1

        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)
        najlepsi_kandidat = najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

        if fitness(najlepsi_kandidat) < fitness(globalne_max):
            zmena += 1
            print(f"Zmena n.{zmena} nastala o: {timeit.default_timer() - start}")
            print(f"Predtym:{fitness(globalne_max)} potom: {fitness(najlepsi_kandidat)}")
            globalne_max = najlepsi_kandidat

        tabu_list.append(najlepsi_kandidat)
        if len(tabu_list) > maxTabuSize:
            popol += 1
            tabu_list.pop()

    print(iteracia, popol, zmena)
    return globalne_max
