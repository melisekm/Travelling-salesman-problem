import random
import timeit
from utils import fitness


class GeneticAlgorithm(list):
    def __init__(self, cities, args):
        print("GENETIC ALGORITHM...")
        self.parse_args(args)  # spracuje argumenty
        self.best_jedinci = []  # zoznam pre vizualizaciu
        iteracia = 0
        init_time = timeit.default_timer()
        generacia = random_generacia(cities, self.velkost_generacie)
        generacia.sort(reverse=True)  # Najvyssia fittnes prva
        while not self.stop(iteracia, init_time):
            krizenie_generacia = Krizenie(generacia, self.pocet_krizeni, self.metoda_vyberu_rodica)
            mutacia_generacia = Mutacia(krizenie_generacia, self.pocet_mutacii, self.mutacia_probability)
            nahodna_generacia = random_generacia(cities, self.pocet_nahodnych)
            self.best_jedinci.append(generacia[0])  # ukladame najlepsieho z generacie pre vizualizaciu
            generacia = self.vyber_najlepsich(
                generacia,
                krizenie_generacia,
                mutacia_generacia,
                nahodna_generacia,
                self.velkost_generacie,
            )
            iteracia += 1
        self.run_time = timeit.default_timer() - init_time
        list.__init__(self, generacia[0])  # vrati list of lists s najlepsim vysledkom

    # Survival of the Fittest, zo vsetkych vygenerovanych odstrani najhorsie
    def vyber_najlepsich(self, najlepsia, krizenie, mutacia, nahodna, velkost):
        survived = najlepsia + krizenie + mutacia + nahodna
        survived.sort(reverse=True)
        return survived[0:velkost]  # cutne od 0 po x

    # vypne po x iteraciach alebo po uplynuti casu
    def stop(self, iteracia, start):
        return iteracia == self.max_iteracii or timeit.default_timer() - start > self.max_trvanie

    def parse_args(self, args):
        self.velkost_generacie = args[0]
        self.pocet_krizeni = args[1]
        self.pocet_mutacii = args[2]
        self.pocet_nahodnych = args[3]
        self.mutacia_probability = args[4]
        self.metoda_vyberu_rodica = args[5]
        self.max_iteracii = args[6]
        self.max_trvanie = args[7]
        metoda = {
            1: "Ruleta",
            2: "Rank",
            3: "Turnaj",
        }
        print(metoda[self.metoda_vyberu_rodica])


# Predstavuje Chromozom - vector navstivenia miest(genov)
class Jedinec(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.cena = fitness(args[0]) ** -1  # obratena hodnota

    def __lt__(self, other):
        return self.cena < other.cena


class Krizenie(list):
    def __init__(self, generacia, velkost, metoda_vyberu_rodica):
        self.metoda_vyberu_rodica = metoda_vyberu_rodica
        list.__init__(self, self.krizenie(generacia, velkost))

    def krizenie(self, generacia, velkost):
        deti = []
        for _ in range(velkost):
            rodicia = VyberRodica(generacia, self.metoda_vyberu_rodica)
            dieta = self.two_point_krizenie(rodicia)
            deti.append(Jedinec(dieta))
        return deti

    def two_point_krizenie(self, rodicia):
        start, end = nahodny_usek(rodicia[0])  # nahodny usek da na korektne miesto
        tmp = [x for x in rodicia[1] if x not in rodicia[0][start:end]]  # odstrani dup
        dieta = tmp[0:start] + rodicia[0][start:end] + tmp[start:]  # vyplni ostatne z rodica1
        return dieta


class Mutacia(list):
    def __init__(self, generacia, velkost, mutacia_probability):
        self.mutacia_probability = mutacia_probability  # na kolko % budu deti mutovat
        list.__init__(self, self.mutacia(generacia, velkost))

    def mutacia(self, generacia, velkost):
        zmutovani = []
        for _ in range(velkost):
            sanca = random.randint(1, 100)
            if sanca <= self.mutacia_probability:  # ak spada do %
                rodic = random.randint(0, len(generacia) - 1)
                dieta = self.otocenie_useku_mutacia(generacia[rodic])
                zmutovani.append(Jedinec(dieta))
        return zmutovani

    def otocenie_useku_mutacia(self, rodic):
        start, end = nahodny_usek(rodic)  # vyberie usek a otoci ho
        dieta = rodic[0:start] + list(reversed(rodic[start:end])) + rodic[end:]
        return dieta


class VyberRodica(list):
    def __init__(self, generacia, metoda_vyberu_rodica):
        self.metoda_vyberu_rodica = metoda_vyberu_rodica
        list.__init__(self, self.vyber_rodicov(generacia))

    def vyber_rodicov(self, generacia):
        if self.metoda_vyberu_rodica == 1:
            return self.ruleta(generacia)
        if self.metoda_vyberu_rodica == 2:
            return self.rank_selection(generacia)
        if self.metoda_vyberu_rodica == 3:
            return self.turnaj(generacia)

    # na zaklade umernosti s fittness vyberie dvoch rodicov
    def ruleta(self, generacia):
        sucet_fitness = 0  # cela ruleta
        for jedinec in generacia:
            sucet_fitness += jedinec.cena
        rodicia = []
        for _ in range(2):  # potrebujem dvoch rodicov
            hod = random.uniform(0, sucet_fitness)  # hadzeme
            priebezny_pocet = 0  # sledujem kam dopadla :)
            for jedinec in generacia:
                priebezny_pocet += jedinec.cena
                if priebezny_pocet >= hod:  # prekrocilo medzisucet
                    rodicia.append(jedinec)
                    break
        return rodicia

    def rank_selection(self, generacia):
        sucet_fitness = (len(generacia) + 1) * len(generacia) / 2
        rodicia = []
        for _ in range(2):  # potrebujem dvoch rodicov
            hod = random.uniform(0, 1)  # hadzeme
            priebezny_pocet = 0  # sledujem kam dopadla :)
            for i, jedinec in enumerate(reversed(generacia), start=1):
                priebezny_pocet += i / sucet_fitness
                if priebezny_pocet >= hod:  # prekrocilo medzisucet
                    rodicia.append(jedinec)
                    break
        return rodicia

    def turnaj(self, generacia):
        n = len(generacia)
        rodicia = []
        for _ in range(2):
            prvy = random.randint(0, n - 1)
            druhy = random.randint(0, n - 1)
            if prvy < druhy:
                rodicia.append(generacia[prvy])
            else:
                rodicia.append(generacia[druhy])
        return rodicia


def random_generacia(cities, velkost):
    generacia = []
    for _ in range(velkost):
        chromozom = cities.copy()  # novy vector
        random.shuffle(chromozom)  # nahodna permutacia
        generacia.append(Jedinec(chromozom))
    return generacia


# vyberie usek v permutacii navstivenia miest, min dlzka 2
def nahodny_usek(state):
    start = random.randint(0, len(state) - 2)
    end = random.randint(start + 1, len(state) - 1)
    return start, end
