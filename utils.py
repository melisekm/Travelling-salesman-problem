import math
import plot_graph


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip().split()  # rozdeli
            cities.append(list(map(float, suradnice)))
    return [City(city[0], city[1]) for city in cities]


def fitness(stav):
    result = 0
    for i in range(len(stav) - 1):
        result += euclidian_d(stav[i], stav[i + 1])
    result += euclidian_d(stav[-1], stav[0])
    return int(round(result))


def euclidian_d(a, b):
    result = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    # return int(round(result))
    return result


def print_riesenie(riesenie):
    for mesto in riesenie:
        print(f"{round(mesto.x, 2)} \t {round(mesto.y, 2)}")
    print(f"Cena riesenia: {fitness(riesenie)}")
    print(f"Hladanie bezalo: {riesenie.run_time}")

    plot_graph.run(riesenie.best_jedinci)
