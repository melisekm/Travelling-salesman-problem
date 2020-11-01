import random
import timeit
import sys

from utils import fitness, GA_utils


class GeneticAlgorithm(list):
    def __init__(self, cities, args):
        print("GENETIC ALGORITHM...")
        self.parseArgs(args)
        start = timeit.default_timer()
        iteracia = 0
        generacia = self.random_generacia(cities, self.velkost_generacie)
        generacia.sort(reverse=True)  # Najvyssia fittnes prva
        best_jedinci = []  # zoznam pre vizualizaciu
        while not self.stop(iteracia, start):
            krizenie_generacia = Krizenie(generacia, self.pocetKrizeni, self.metoda_vyberu_rodica)
            mutacia_generacia = Mutacia(krizenie_generacia, self.pocetMutacii, self.mutacia_probability)
            nahodna_generacia = self.random_generacia(cities, self.pocetNahodnych)
            best_jedinci.append(generacia[0])  # ukladame najlepsieho z generacie

            generacia = self.vyber_najlepsich(
                generacia,
                krizenie_generacia,
                mutacia_generacia,
                nahodna_generacia,
                self.velkost_generacie,
            )

            iteracia += 1

        sys.stdout = sys.__stdout__
        GA_utils(generacia[0], start, best_jedinci)  # print info
        list.__init__(self, generacia[0])

    def vyber_najlepsich(self, najlepsia, krizenie, mutacia, nahodna, velkost):
        survived = najlepsia + krizenie + mutacia + nahodna
        survived.sort(reverse=True)
        return survived[0:velkost]

    def random_generacia(self, cities, velkost):
        generacia = []
        for _ in range(velkost):
            chromozom = cities.copy()  # mozno nechat prveho byt?
            random.shuffle(chromozom)
            generacia.append(Jedinec(chromozom))
        return generacia

    def stop(self, iteracia, start):
        return iteracia == self.max_iteracii or timeit.default_timer() - start > 30

    def parseArgs(self, args):
        self.velkost_generacie = args[0]
        self.pocetKrizeni = args[1]
        self.pocetMutacii = args[2]
        self.pocetNahodnych = args[3]
        self.mutacia_probability = args[4]
        self.metoda_vyberu_rodica = args[5]
        self.max_iteracii = args[6]


class Jedinec(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.cena = fitness(args[0]) ** -1

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
        start, end = nahodny_usek(rodicia[0])
        tmp = [x for x in rodicia[1] if x not in rodicia[0][start:end]]
        dieta = tmp[0:start] + rodicia[0][start:end] + tmp[start:]
        return dieta


class Mutacia(list):
    def __init__(self, generacia, velkost, mutacia_probability):
        self.mutacia_probability = mutacia_probability
        list.__init__(self, self.mutacia(generacia, velkost))

    def mutacia(self, generacia, velkost):
        zmutovani = []
        for _ in range(velkost):
            sanca = random.randint(1, 100)
            if sanca <= self.mutacia_probability:
                rodic = random.randint(0, len(generacia) - 1)
                dieta = self.otocenie_useku_mutacia(generacia[rodic])
                zmutovani.append(Jedinec(dieta))
        return zmutovani

    def otocenie_useku_mutacia(self, rodic):
        start, end = nahodny_usek(rodic)
        dieta = rodic[0:start] + list(reversed(rodic[start:end])) + rodic[end:]
        return dieta


class VyberRodica(list):
    def __init__(self, generacia, metoda_vyberu_rodica):
        self.metoda_vyberu_rodica = metoda_vyberu_rodica
        list.__init__(self, self.vyber_rodicov(generacia))

    def vyber_rodicov(self, generacia):
        if self.metoda_vyberu_rodica == 1:
            return self.ruleta(generacia)
        elif self.metoda_vyberu_rodica == 2:
            return self.TODO(generacia)

    def ruleta(self, generacia):
        sucet_fitness = 0
        for jedinec in generacia:
            sucet_fitness += jedinec.cena
        rodicia = []
        for _ in range(2):
            hod = random.uniform(0, sucet_fitness)
            priebezny_pocet = 0
            for jedinec in generacia:
                priebezny_pocet += jedinec.cena
                if priebezny_pocet >= hod:
                    rodicia.append(jedinec)
                    break
        return rodicia

    def TODO(self, generacia):
        pass


def nahodny_usek(state):
    start = random.randint(0, len(state) - 2)
    end = random.randint(start + 1, len(state) - 1)
    return start, end
