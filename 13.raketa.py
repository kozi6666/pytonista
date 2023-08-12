from random import randint


class Rocket:
    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed

    def moveup(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta na wysokości: " + str(self.altitude)


rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketsIndexToMove = randint(0, len(rockets) - 1)
    rockets[rocketsIndexToMove].moveup()

for rocket in rockets:
    print(rocket)

rocket = Rocket()
