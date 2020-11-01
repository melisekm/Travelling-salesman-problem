import os
import glob
import matplotlib.pyplot as plt
import utils


def run(best_jedinci):
    print("Triedim..")

    uniq = [best_jedinci[0]]
    prev = utils.fitness(best_jedinci[0])
    for jedinec in best_jedinci:
        if prev != utils.fitness(jedinec):
            uniq.append(jedinec)
        prev = utils.fitness(jedinec)

    files = glob.glob("../images/*")
    if len(files) != len(uniq):
        for f in files:
            os.remove(f)
    print("Vytvaram obrazky..")
    for index, jedinec in enumerate(uniq):
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
        plt.savefig(f"../images/stav-{index}.jpg")
        plt.close()

    print("Done")
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
