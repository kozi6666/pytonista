import random

list = [1, 2, 3, 4, 5, 6]
x = 1

while True:
    req = input("...")
    if req == "":
        print(f"{x}"" Rzut kostką")
        print("")
        print(random.choice(list))
        x += 1
        continue
    elif req == "q":
        break
    else:
        continue