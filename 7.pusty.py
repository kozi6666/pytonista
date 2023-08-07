import random

list = [1, 2, 3, 4, 5, 6]
x = 1
nums = []
suming = sum(nums)

def game():
    print("")
    print("Witaj w grze BLACKJACK")
    print("")
    print("Wciśnij <enter> aby zacząć gre")


def throw(suming,):
    req = input("...")
    x = 1
    while True:
        if req == "":
            print(f"{x}"" Rzut kostką")
            print("")
            num = (random.choice(list))
            print(num)
            nums.append(num)
            x += 1
            suming = sum(nums)
            print("")
            print("Twoje punkty: ", suming)
            continue

        elif req == "q":
            print("Twój ostateczny wynik to:", suming)
            break
        elif suming == 21:
            print("Gratulacje! Osiągąłeś maxymalną liczbę punktów")
            break
        elif suming < 21:
            print("Przegrałeś! Niestety przekroczyłeś 21 punktów")
            break
        else:
            continue

def suming():
    while suming == 21:
    print("Gratulacje! Osiągąłeś maxymalną liczbę punktów")
    exit()

    while suming < 21:
    print("Przegrałeś! Niestety przekroczyłeś 21 punktów")
    exit()