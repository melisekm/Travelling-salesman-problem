import tabu_search
import timeit


def parse_input(path):
    cities = []
    with open(path, "r") as file:
        for line in file:
            suradnice = line.strip("").split()  # odignoruje () a rozdeli
            cities.append(list(map(float, suradnice)))
    return cities


if __name__ == "__main__":
    cities = parse_input("vstup.txt")
    start = timeit.default_timer()
    riesenie = tabu_search.run(cities, 100)
    end = timeit.default_timer()
    print(end - start)
    for mesto in riesenie:
        print(f"{mesto.x}\t {mesto.y}")
    print(f"cena riesenia: {tabu_search.fitness(riesenie)}")
