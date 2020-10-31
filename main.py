import timeit
import tabu_search

from utils import fitness


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip("").split()  # rozdeli
            cities.append(list(map(float, suradnice)))
    return cities


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    start = timeit.default_timer()
    riesenie_tabu = tabu_search.run(cities, 500)
    end = timeit.default_timer()
    print(end - start)
    for mesto in riesenie_tabu:
        print(f"{mesto.x}\t {mesto.y}")
    print(f"cena riesenia: {fitness(riesenie_tabu)}")
