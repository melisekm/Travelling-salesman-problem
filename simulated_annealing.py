import random
import timeit
import math

from utils import fitness


class SimulatedAnnealing(list):
    def __init__(self, cities, args):
        self.name = "SIMULATED ANNEALING..."
        self.parse_args(args)  # spracuje argumenty
        self.best_jedinci = []  # zoznam pre vizualizaciu
        init_time = timeit.default_timer()
        rozvrh = Rozvrh(self.ochladenie, len(cities), self.min_teplota)
        random.shuffle(cities)
        current = Stav(cities)
        teplota = rozvrh.pociatocna_teplota

        while not self.stop(teplota, rozvrh.min_teplota, init_time):
            sused = self.vyber_nasledovnika(current)
            delta = sused.fitness - current.fitness
            if delta > 0 or self.probabilita(delta, teplota):
                current = sused
            self.best_jedinci.append(current)  # ukladame pre vizualizaciu
            teplota *= rozvrh.ochladenie

        self.run_time = timeit.default_timer() - init_time
        list.__init__(self, current)

    def vyber_nasledovnika(self, stav):
        start, end = nahodny_usek(stav)  # vyberie usek a otoci ho
        dieta = stav[0:start] + list(reversed(stav[start:end])) + stav[end:]
        return Stav(dieta)

    def probabilita(self, delta, teplota):
        probabilita = math.exp(delta / teplota)
        rand = random.uniform(0, 1)
        if probabilita >= rand:
            return True
        else:
            return False

    def stop(self, teplota, min_teplota, start):
        return teplota < min_teplota or timeit.default_timer() - start > self.max_trvanie

    def parse_args(self, args):
        self.ochladenie = args[0]
        self.min_teplota = args[1]
        self.max_trvanie = args[2]


class Stav(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.fitness = fitness(args[0]) ** -1  # obratena hodnota


class Rozvrh:
    def __init__(self, ochladenie, velkost, min_teplota):
        self.ochladenie = 1 - ochladenie
        self.pociatocna_teplota = math.sqrt(velkost)
        self.min_teplota = min_teplota


# vyberie usek v permutacii navstivenia miest, min dlzka 2
def nahodny_usek(state):
    start = random.randint(0, len(state) - 2)
    end = random.randint(start + 1, len(state) - 1)
    return start, end
