import random

lista_slow = ["kocham dominike czube"]


def wylosuj_slowo():
    return random.choice(lista_slow)


def gra():
    slowo = wylosuj_slowo()
    zgadniete_litery = []
    proba = 0

    while True:
        pokaz = ""
        for litera in slowo:
            if litera in zgadniete_litery:
                pokaz += litera
            elif litera == " ":
                pokaz += " "
            else:
                pokaz += "_"

        if pokaz == slowo:
            print("\nGRATULACJE! ZGADŁEŚ!: ", slowo)
            break

        print("\nSłowo lub zdanie: ", pokaz)

        zgadniecie = input("Zgadnij literę lub zdanie: ").lower()

        if zgadniecie == slowo:
            print("\nGRATULACJE! ZGADŁEŚ!: ", slowo)
            break

        if zgadniecie in zgadniete_litery:
            print("\nTa litera została juz wpisana")
            continue

        zgadniete_litery.append(zgadniecie)

        if zgadniecie not in slowo:
            proba += 1

            print("\nNie ma tu takiej litery")
            if proba == 6:
                print("\nPRZEGRAŁEŚ! Słowo lub zdanie to: ", slowo)
                break


if __name__ == "__main__":
    print("\nWITAJ W GRZE 'WISIELEC' ! ")
    print("Życzę powodzenia!")

    gra()
