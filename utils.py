import math

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


def load_input():
    print("Koniec [q]")
    print("Predvygenerovane: [default20] [wi29] [att48] [berlin52]")
    print("alebo [vlastny] zo suboru tests - vlastny.txt")
    vstup = input()
    if vstup in ("default20", "wi29", "att48", "berlin52"):
        path = "tests/" + vstup + ".txt"
    elif vstup == "vlastny":
        path = "tests/vlastny.txt"
    elif vstup == "q":
        print("Ukoncujem")
        quit()
    else:
        return [None] * 3
    cities = parse_input(path)
    print(f"{path} nacitane. Pocet miest:{len(cities)}")
    print("Zvolte si metodu:")
    print("Geneticky algoritmus[GA]")
    print("Simulovane zihanie[SA]")
    print("Tabu search[TABU]")
    print("Vsetky naraz [VSETKY]")
    metoda = input()
    if metoda.lower() not in ("ga", "sa", "tabu", "vsetky"):
        return [None] * 3
    print("Vykonavam...")
    return vstup, cities, metoda


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
    riesenie_cena = int(round(fitness(riesenie)))
    opt = vstup in optimal
    for mesto in riesenie:
        print(f"{round(mesto.x, 2)} \t {round(mesto.y, 2)}")
    print(riesenie.name)
    print(f"Cena riesenia: {riesenie_cena}")
    if opt is True:
        print(f"Optimalne riesenie: {optimal.get(vstup)}")
        print(f"Presnost: {((optimal.get(vstup) / riesenie_cena) * 100):.3f}%")
    print(f"Hladanie bezalo: {riesenie.run_time}")
