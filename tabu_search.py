import random
import timeit
import sys

from utils import fitness


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


def stop(nevylepsil, stopAt, start):
    return nevylepsil == stopAt or timeit.default_timer() - start > 30


def run(cities, maxTabuSize):
    maxTabuSize = 500
    stopAt = 1000
    nevylepsil = 0
    random.shuffle(cities)  # vygenerovanie nahodneho vektoru
    globalne_max = cities  # sBest
    najlepsi_kandidat = cities  # bestCandidate
    tabu_list = [cities]  # tabuList
    sys.stdout = open("globalne_max.txt", "w")
    sys.stdout = open("best_candidate.txt", "w")
    start = timeit.default_timer()
    while not stop(nevylepsil, stopAt, start):

        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)
        najlepsi_kandidat = najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

        najlepsi_kandidat_fitness = fitness(najlepsi_kandidat)
        globalne_max_fitness = fitness(globalne_max)

        sys.stdout = open("best_candidate.txt", "a")
        print(f"{round(timeit.default_timer() - start,2)} {najlepsi_kandidat_fitness} {len(tabu_list)}")

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
