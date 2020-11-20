import math
import plot_graph

optimal = {
    "default20": 896,
    "wi29": 27601,
    "att48": 33522,
    "berlin52": 7544,
}


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
    return result


def euclidian_d(a, b):
    result = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    return result


def print_riesenie(riesenie, vstup):
    riesenie_cena = fitness(riesenie)
    opt = vstup in optimal
    for mesto in riesenie:
        print(f"{round(mesto.x, 2)} \t {round(mesto.y, 2)}")
    print(riesenie.name)
    print(f"Cena riesenia: {riesenie_cena}")
    if opt is True:
        print(f"Optimalne riesenie: {optimal.get(vstup)}")
        print(f"Presnost: {((optimal.get(vstup) / riesenie_cena) * 100):.3f}%")
    print(f"Hladanie bezalo: {riesenie.run_time}")

    # plot_graph.run(riesenie.best_jedinci)
