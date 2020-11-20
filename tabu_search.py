import random
import timeit
from utils import fitness


class TabuSearch(list):
    def __init__(self, cities, args):
        self.name = "TABU SEARCH..."
        self.parse_args(args)
        self.best_jedinci = []
        random.shuffle(cities)  # vygenerovanie nahodneho vektoru
        globalne_max = cities
        najlepsi_kandidat = cities
        tabu_list = [cities]
        nevylepsil = 0
        init_time = timeit.default_timer()
        while not self.stop(nevylepsil, init_time):
            nasledovnici = self.vygeneruj_nasledovnikov(najlepsi_kandidat)
            najlepsi_kandidat = self.najdi_najlepsieho_kandidata(nasledovnici, tabu_list)

            najlepsi_kandidat_fitness = fitness(najlepsi_kandidat)
            globalne_max_fitness = fitness(globalne_max)

            if najlepsi_kandidat_fitness < globalne_max_fitness:
                globalne_max = najlepsi_kandidat
                nevylepsil = 0

            tabu_list.append(najlepsi_kandidat)
            if len(tabu_list) > self.max_tabu_size:
                tabu_list.pop(0)
            nevylepsil += 1
        self.run_time = timeit.default_timer() - init_time
        list.__init__(self, globalne_max)

    def vygeneruj_nasledovnikov(self, stav):
        rand = random.randint(0, len(stav) - 1)
        nasledovnici = []
        for i in range(0, len(stav)):
            if i != rand:
                nasledovnik = stav.copy()
                nasledovnik[i], nasledovnik[rand] = nasledovnik[rand], nasledovnik[i]
                nasledovnici.append(nasledovnik)
        return nasledovnici

    def najdi_najlepsieho_kandidata(self, nasledovnici, tabu_list):
        kandidat = nasledovnici[0]
        for nasledovnik in nasledovnici:
            if nasledovnik not in tabu_list and fitness(nasledovnik) < fitness(kandidat):
                kandidat = nasledovnik
        return kandidat

    def stop(self, nevylepsil, start):
        return nevylepsil == self.max_iteracii or timeit.default_timer() - start > self.max_trvanie

    def parse_args(self, args):
        self.max_tabu_size = args[0]
        self.max_iteracii = args[1]
        self.max_trvanie = args[2]
