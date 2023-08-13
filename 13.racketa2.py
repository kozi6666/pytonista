from raketa import Rocket
from random import randint

rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketsIndexToMove = randint(0, len(rockets) - 1)
    rockets[rocketsIndexToMove].moveup()

for rocket in rockets:
    print(rocket)

rocket = Rocket()