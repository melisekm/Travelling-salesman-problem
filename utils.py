import math
import timeit
import plot_graph


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip("").split()  # rozdeli
            cities.append(list(map(float, suradnice)))
    return [City(city[0], city[1]) for city in cities]


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
    end = timeit.default_timer()
    for mesto in najlepsi:
        print(f"{mesto.x}\t {mesto.y}")
    print(f"cena riesenia: {fitness(najlepsi)}")
    print(f"Hladanie bezalo: {end - start}")

    plot_graph.run(best_jedinci)
