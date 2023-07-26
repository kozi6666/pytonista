import random


def get_wybor_gracza():
    wybor = input("k , p, n")
    while wybor not in ['k', 'p', 'n']:
        print("bledny wybor")
        wybor = input("k , p, n")
    return wybor


def get_wybor_komp():
    return random.choice(['k', 'p', 'n'])


def zwycieza(wybor, komp):
    if wybor == komp:
        return "Remis!"
    elif (wybor == 'k' and komp == 'n') or \
            (wybor == 'p' and komp == 'k') or \
            (wybor == 'n' and komp == 'p'):
        return "Wygrałeś"
    else:
        return "komp wygral"


def gra():
    wybor = get_wybor_gracza()
    komp = get_wybor_komp()
    print(f"twoj wybor: {wybor}")
    print(f"wybor kompa: {komp}")
    print(zwycieza(wybor, komp))


while True:
    if __name__ == "__main__":
        gra()
    continue
