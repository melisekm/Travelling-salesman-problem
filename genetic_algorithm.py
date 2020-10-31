import random
import timeit
import sys

from utils import fitness

# metody vyberu rodica su:
# 1 - ruleta?
# 2 - turnaj

metoda_vyberu_rodica = 1
mutacia_probability = 10


class Jedinec(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.cena = fitness(args[0]) ** -1

    def __lt__(self, other):
        return self.cena < other.cena


def random_generacia(cities, velkost):
    generacia = []
    for _ in range(velkost):
        chromozom = cities.copy()  # mozno nechat prveho byt?
        random.shuffle(chromozom)
        generacia.append(Jedinec(chromozom))
    return generacia


def ruleta(generacia):
    sucet_fitness = 0
    for jedinec in generacia:
        sucet_fitness += jedinec.cena
    rodicia = []
    for _ in range(2):
        hod = random.uniform(0, sucet_fitness)
        priebezny_pocet = 0
        for jedinec in generacia:
            priebezny_pocet += jedinec.cena
            if priebezny_pocet >= hod:
                rodicia.append(jedinec)
                break
    return rodicia


def TODO(generacia):
    pass


def nahodny_usek(state):
    start = random.randint(0, len(state) - 2)
    end = random.randint(start + 1, len(state) - 1)
    return start, end


def vyber_rodicov(generacia):
    if metoda_vyberu_rodica == 1:
        return ruleta(generacia)
    elif metoda_vyberu_rodica == 2:
        return TODO(generacia)


def two_point_krizenie(rodicia):
    start, end = nahodny_usek(rodicia[0])
    tmp = [x for x in rodicia[1] if x not in rodicia[0][start:end]]
    dieta = tmp[0:start] + rodicia[0][start:end] + tmp[start:]
    return dieta


def krizenie(generacia, velkost):
    deti = []
    for _ in range(velkost):
        rodicia = vyber_rodicov(generacia)
        dieta = two_point_krizenie(rodicia)
        deti.append(Jedinec(dieta))
    return deti


def otocenie_useku_mutacia(rodic):
    start, end = nahodny_usek(rodic)
    dieta = rodic[0:start] + list(reversed(rodic[start:end])) + rodic[end:]
    return dieta


def mutacia(generacia, velkost):
    zmutovani = []
    for _ in range(velkost):
        sanca = random.randint(1, 100)
        if sanca <= mutacia_probability:
            rodic = random.randint(0, len(generacia) - 1)
            dieta = otocenie_useku_mutacia(generacia[rodic])
            zmutovani.append(Jedinec(dieta))
    return zmutovani


def vyber_najlepsich(najlepsia, krizenie, mutacia, nahodna, velkost):
    survived = najlepsia + krizenie + mutacia + nahodna
    survived.sort(reverse=True)
    return survived[0:velkost]


def stop(iteracia, stopAt, start):
    return iteracia == stopAt or timeit.default_timer() - start > 30


def run(cities):
    start = timeit.default_timer()
    iteracia = 0
    stopAt = 1000
    generacia = random_generacia(cities, 50)
    generacia.sort(reverse=True)
    while not stop(iteracia, stopAt, start):
        krizenie_generacia = krizenie(generacia, 32)
        mutacia_generacia = mutacia(krizenie_generacia, 14)
        nahodna_generacia = random_generacia(cities, 4)
        generacia = vyber_najlepsich(
            generacia, krizenie_generacia, mutacia_generacia, nahodna_generacia, 50
        )

        iteracia += 1

    return generacia[0]
