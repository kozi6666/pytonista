import random


lista_slow = ["kochamdominikeczube"]


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
            else:
                pokaz += "_"

        if pokaz == slowo:
            print("gratulacje! odgadles: ", slowo)
            break

        print("slowo: ", pokaz)

        zgadniecie = input("zgadnij litere lub całość: ").lower()

        if zgadniecie == slowo:
            print("gratulacje! odgadles: ", slowo)
            break

        if zgadniecie in zgadniete_litery:
            print("ta litera zostala juz odgadnieta")
            continue

        zgadniete_litery.append(zgadniecie)

        if zgadniecie not in slowo:
            proba += 1
            print("nie ma takiej litery")
            if proba == 6:
                print("przegrales! to: ", slowo)
                break


if __name__ == "__main__":
    print("Witaj w grze 'Wisielec' ! ")
    gra()
