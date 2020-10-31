import random
import timeit
import sys

from utils import City, fitness


def random_generacia(cities, velkost):
    generacia = []
    for _ in range(velkost):
        chromozom = cities.copy()
        random.shuffle(chromozom)
        generacia.append(chromozom)
    return generacia


def krizenie(generacia, velkost):
    pass


def mutacia(generacia, velkost):
    pass


def vyber_najlepsich(najlepsia, krizenie, mutacia, nahodna, velkost):
    pass


def najdi_najlepsi(generacia):
    pass


def stop(iteracia, stopAt, start):
    return iteracia == stopAt or timeit.default_timer() - start > 30


def run(cities):
    start = timeit.default_timer()
    iteracia = 0
    stopAt = 1000
    prva_generacia = random_generacia(cities, 50)
    globalne_max = prva_generacia
    while not stop(iteracia, stopAt, start):
        krizenie_generacia = krizenie(globalne_max, 32)
        mutacia_generacia = mutacia(krizenie_generacia, 14)
        nahodna_generacia = random_generacia(cities, 4)
        globalne_max = vyber_najlepsich(
            globalne_max, krizenie_generacia, mutacia_generacia, nahodna_generacia, 50
        )

        iteracia += 1

    return najdi_najlepsi(globalne_max)