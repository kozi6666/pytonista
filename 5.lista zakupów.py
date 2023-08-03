def wyswietl(lista):
    print("")
    print("Lista zakupów: ")
    for indeks, produkt in enumerate(lista, start=1):
        print(f"{indeks}. {produkt}")


def dodaj(lista, produkt):
    lista.append(produkt)
    print("")
    print(f"Dodano produkt: '{produkt}' do listy zakupów")


def usun(lista, produkt):
    if produkt in lista:
        lista.remove(produkt)
        print("")
        print(f"Usunięto produkt: '{produkt}' z listy zakupów")
    else:
        print("")
        print(f"Produkt: '{produkt}' nie znajduje się na liście zakupów")


if __name__ == "__main__":
    lista = []

    while True:
        print("")
        print("Co chcesz kupić?")
        print("")
        print("1. Wyświetl listę")
        print("2. Dodaj produkt")
        print("3. Usuń produkt")
        print("")
        print("4. Zakończ program")
        print("")
        wybor = input("Twoj wybór: ")

        if wybor == "1":
            wyswietl(lista)
        elif wybor == "2":
            produkt = input("Wprowadź nazwę produktu, który chcesz dodać: ")
            dodaj(lista, produkt)
        elif wybor == "3":
            produkt = input("Wprowadź nazwę produktu, który chcesz usunąć: ")
            usun(lista, produkt)
        elif wybor == "4":
            print("DZIĘKUJĘ ZA SKORZYSTANIE")
            print("Koniec programu")
            break
        else:
            print("Nieprawidłowy wybór")
