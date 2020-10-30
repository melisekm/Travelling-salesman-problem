import math
import random


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, vector):
        self.vector = vector
        self.fitness = calculate_fitness(vector)

    def calculate_fitness(vector):
        pass

    def euclidian_d(city_A, city_B):
        return math.sqrt((city_A.x - city_B.x) ** 2 + (city_A.y - city_B.y) ** 2)


def vygenerujNasledovnikov(parent):
    nasledovnici = []

    for i in range(1, len(parent)):
        for j in range(i + 1, len(parent)):
            nasledovnik = parent.copy()
            nasledovnik[i], nasledovnik[j] = nasledovnik[j], nasledovnik[i]
            nasledovnici.append(nasledovnik)

    return nasledovnici


def run(cities, maxTabuSize):
    riesenie = None
    maxTabuSize = 100
    nahodny = [City(city[0], city[1]) for city in cities]
    globalne_max = nahodny
    najlepsi_kandidat = nahodny
    tabuList = []
    tabuList.append(nahodny)

    while True:
        nasledovnici = vygenerujNasledovnikov(najlepsi_kandidat)