import tabu_search


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip("()\n").split(", ")  # odignoruje () a rozdeli
            cities.append(suradnice)
    return cities


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    tabu_search.run(cities, 100)
