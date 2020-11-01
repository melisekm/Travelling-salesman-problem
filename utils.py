import math
import timeit
import plotGraph


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


def GA_utils(najlepsi, start, best_jedinci):
    for mesto in najlepsi:
        print(f"{mesto.x}\t {mesto.y}")
    print(f"cena riesenia: {fitness(najlepsi)}")
    end = timeit.default_timer()
    print(end - start)
    plotGraph.run(best_jedinci)
