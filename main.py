import tabu_search
import genetic_algorithm

from utils import City


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip("").split()  # rozdeli
            cities.append(list(map(float, suradnice)))
    return [City(city[0], city[1]) for city in cities]


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    # riesenie_tabu = tabu_search.run(cities, 500)
    print("GENETIC ALGORITHM...")
    riesenie_genetic = genetic_algorithm.run(cities)
