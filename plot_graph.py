import os
import glob
import matplotlib.pyplot as plt
import utils


def run(best_jedinci):
    vstup = input("Chcete vytvorit obrazky?: ")
    if vstup != "y":
        return
    uniq = vytried(best_jedinci)  # odstrani duplikaty na zaklade fitness
    zmaz_stare(uniq)  # sem len dlzka aby vedel kolko
    vytvor_obrazky(uniq)  # tuto je tiez kopa custom veci
    vytvor_video(uniq)  # pozor na nazov obrazkov a cestu k nim


def vytvor_obrazky(uniq):
    print("Vytvaram obrazky..")
    indexx = 0
    if len(uniq) > 1000:
        prev = uniq[0].fitness
    for index, jedinec in enumerate(uniq):
        if len(uniq) > 1000:
            if index > len(uniq) - 50:
                pass
            elif jedinec.fitness < prev:
                continue
            if index < len(uniq) - 50 and index % 3 == 0:
                continue
            prev = jedinec.fitness
        indexx += 1
        x = []
        y = []
        for point in jedinec:
            x.append(point.x)
            y.append(point.y)
        x.append(jedinec[0].x)
        y.append(jedinec[0].y)
        plt.title(f"cena{utils.fitness(jedinec)}")
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.savefig(f"../images/stav-{indexx}.jpg")
        plt.close()
    print("Done")


def zmaz_stare(uniq):
    files = glob.glob("../images/*")
    if len(files) != len(uniq):
        for f in files:
            os.remove(f)


def vytried(best_jedinci):
    print("Triedim..")
    uniq = [best_jedinci[0]]
    prev = utils.fitness(best_jedinci[0])
    for jedinec in best_jedinci:
        if prev != utils.fitness(jedinec):
            uniq.append(jedinec)
        prev = utils.fitness(jedinec)
    return uniq


def vytvor_video(uniq):
    video = input("Chcete vytvorit video? ffmpeg je potrebny: ")
    if video == "y":
        if len(uniq) > 40:
            rychlost = 5  # je to skor rychlost spomalenia :D
        else:
            rychlost = 8
        os.system(
            'cmd /c "C:/Users/melis/Desktop/ffmpeg/bin/ffmpeg.exe -loglevel quiet -y -f image2 -i "C:/Users/melis/Desktop/Dropbox/5.semester/UI/Zadanie 3/images/stav-%d.jpg" -vcodec libx264 -b 800k  -vf "setpts='
            + str(rychlost)
            + '*PTS" video.avi"'
        )
        preview = input("Preview?: ")
        if preview == "y":
            os.system(r'cmd /c "C:\Users\melis\Desktop\ffmpeg\bin\ffplay.exe -loglevel quiet video.avi')
