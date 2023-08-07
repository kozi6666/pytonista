import random

list = [1, 2, 3, 4, 5, 6]
x = 1
nums = []
suming = sum(nums)

print("")
print("Witaj w grze BLACKJACK")
print("")
print("Wciśnij <enter> aby zacząć gre")

while suming <= 21:
    req = input("...")
    if req == "":
        print(f"{x}"" Rzut kostką")
        print("")
        num = (random.choice(list))
        print("Wyrzuciłeś:",num)
        nums.append(num)
        x += 1
        suming = sum(nums)
        print("")
        print("Twoje punkty: ", suming)

        continue
    elif req == "q":
        print("Twój ostateczny wynik to:", suming)
        break
    else:
        continue

while suming == 21:
    print("Gratulacje! Osiągąłeś maxymalną liczbę punktów")
    break
while suming > 21:
    print("Przegrałeś! Niestety przekroczyłeś 21 punktów")
    break
