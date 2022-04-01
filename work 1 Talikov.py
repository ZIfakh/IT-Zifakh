class Bullet:
    def __init__(self, caliber, mass):
        self.caliber = caliber
        self.mass = mass
        self.power = self.caliber * self.mass * 10


class Clip(Bullet):
    def __init__(self):
        #Будем использовать стек
        self.mag = []

    def add(self, Bullet):
        self.mag.append(Bullet)

    def remove(self):
        if len(self.mag > 0):
            self.mag.pop(-1)
        else:
            print("Обойма пуста")


newClip = Clip()

newClip.add(Bullet(9, 0.01))
newClip.add(Bullet(7, 0.005))
newClip.add(Bullet(12, 0.02))

def writeFile():
    f = open("output.txt", "w")
    global newClip
    f.write("В обойме " + str(len(newClip.mag)) + " снарядов:\n")
    for i in range(len(newClip.mag)):
        f.write("Снаряд " + str(i + 1) + ": " + str(newClip.mag[i].caliber) + ", " + str(newClip.mag[i].mass) + ", " + str(newClip.mag[i].power) + "\n")
    f.close()

writeFile()

