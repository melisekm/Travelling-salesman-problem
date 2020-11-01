import random
import timeit
import sys
import math

from utils import fitness


class Rozvrh:
    def __init__(self, velkost):
        self.ochladenie = 0.9995
        self.pociatocna_teplota = math.sqrt(velkost)
        self.min_teplota = 1e-8


class Stav(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.fitness = fitness(args[0]) ** -1  # obratena hodnota


def stop(start):
    return timeit.default_timer() - start > 30


def vyber_nasledovnika(stav):
    rand1 = random.randint(0, len(stav) - 1)
    rand2 = random.randint(0, len(stav) - 1)

    nasledovnik = stav.copy()
    nasledovnik[rand1 : (rand1 + rand2)] = reversed(nasledovnik[rand1 : (rand1 + rand2)])
    return Stav(nasledovnik)


def probability(delta, teplota):
    probabilita = math.exp(delta / teplota)
    rand = random.uniform(0, 1)
    if probabilita >= rand:
        return True
    else:
        return False


def run(cities):
    rozvrh = Rozvrh(len(cities))
    initTime = timeit.default_timer()
    random.shuffle(cities)
    current = Stav(cities)
    teplota = rozvrh.pociatocna_teplota
    # vsetky = []
    while not stop(initTime):
        if teplota < rozvrh.min_teplota:
            break
        sused = vyber_nasledovnika(current)
        delta = sused.fitness - current.fitness
        if delta > 0 or probability(delta, teplota):
            current = sused
        # vsetky.append(current)
        teplota *= rozvrh.ochladenie

    print(timeit.default_timer() - initTime)
    # vsetky = vytried(vsetky)
    # sys.stdout = open("GA.txt", "w")
    # for i in vsetky:
    #    print(fitness(i))

    sys.stdout = sys.__stdout__
    return current


def vytried(best_jedinci):
    print("Triedim..")
    uniq = [best_jedinci[0]]
    prev = fitness(best_jedinci[0])
    for jedinec in best_jedinci:
        if prev != fitness(jedinec):
            uniq.append(jedinec)
        prev = fitness(jedinec)
    return uniq