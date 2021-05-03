import random
import timeit
import math

from utils import fitness


class SimulatedAnnealing(list):
    def __init__(self, cities, args):
        self.name = "SIMULATED ANNEALING..."
        self.parse_args(args)  # spracuje argumenty
        init_time = timeit.default_timer()
        rozvrh = Rozvrh(self.ochladenie, self.min_teplota, self.max_teplota)  # rovzvrh teploty
        random.shuffle(cities)  # nahodny vektor
        current = Stav(cities)
        teplota = rozvrh.pociatocna_teplota

        while not self.stop(teplota, rozvrh.min_teplota, init_time):
            sused = self.vyber_nasledovnika(current)
            delta = sused.fitness - current.fitness
            if delta > 0 or self.probabilita(delta, teplota):
                current = sused  # akceptuj iba ak je lepsi alebo teplota dost nizka
            teplota *= rozvrh.ochladenie

        self.run_time = timeit.default_timer() - init_time
        list.__init__(self, current)

    # vyberie nahodny usek a otoci ho
    def vyber_nasledovnika(self, stav):
        start, end = nahodny_usek(stav)  # vyberie usek a otoci ho
        dieta = stav[0:start] + list(reversed(stav[start:end])) + stav[end:]
        return Stav(dieta)

    # funkcia pravdepodobnosti prijatia horsieho riesenia
    def probabilita(self, delta, teplota):
        sanca = math.exp(delta / teplota)
        rand = random.uniform(0, 1)
        return True if sanca >= rand else False

    def stop(self, teplota, min_teplota, start):
        return teplota < min_teplota or timeit.default_timer() - start > self.max_trvanie

    def parse_args(self, args):
        self.ochladenie = args[0]
        self.max_teplota = args[1]
        self.min_teplota = args[2]
        self.max_trvanie = args[3]


class Stav(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.fitness = fitness(args[0]) ** -1  # obratena hodnota


class Rozvrh:
    def __init__(self, ochladenie, min_teplota, max_teplota):
        self.ochladenie = 1 - ochladenie
        self.pociatocna_teplota = max_teplota
        self.min_teplota = min_teplota


# vyberie usek v permutacii navstivenia miest, min dlzka 2
def nahodny_usek(state):
    start = random.randint(0, len(state) - 2)
    end = random.randint(start + 1, len(state) - 1)
    return start, end
