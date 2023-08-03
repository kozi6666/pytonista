import datetime
import time


def odliczanie(czas):
    while czas > 0:
        print("")
        print("Pozostało:", czas, "sekund")
        print("")
        time.sleep(1)
        czas -= 1

    print("Odliczanie zakończone")


def zapetlonyzegar():
    while True:
        czestotliwosc = 1
        jestgodzina = datetime.datetime.now().strftime("%H:%M:%S""    ""data: ""%d-%m-%Y")
        print("")
        print("Jest godzina:", jestgodzina)
        print("")
        time.sleep(czestotliwosc)


while True:
    print("")
    print("Zegar")
    print("")
    print("Dostepne operacje: ")
    print("1. Aktualna godzina")
    print("2. Sekundnik")
    print("0. Wyjście")
    wybor = input("WYBIERZ NUMER OPERACJI: ")

    if wybor not in ("2", "1", "0"):
        print("NIEPOPRAWNY WYBÓR")
        continue

    if wybor == "0":
        print("DZIEKUJEMY ZA KORZYSTANIE Z ZEGARA")
        break

    if wybor == "2":
        czas_do_odliczania = int(input("Ile sekund odliczyć: "))
        odliczanie(czas_do_odliczania)

    if wybor == "1":
        zapetlonyzegar()
