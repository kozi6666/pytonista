import re
def kalkulator_wyrazenia(wyrazenie):
    try:
        wyrazenie = re.sub(r'\s+', '', wyrazenie)
        wynik = eval(wyrazenie)
        return wynik
    except Exception as e:
        return f"Błąd: {str(e)}"


while True:
    print("")
    print("KALKULATOR")
    print("Dostepne operacje: ")
    print("1. Wyrażenie")
    print("0. Wyjście")
    wybor = input("WYBIERZ NUMER OPERACJI: ")

    if wybor not in ("1", "0"):
        print("NIEPOPRAWNY WYBÓR")
        continue

    if wybor == "0":
        print("DZIĘKUJĘ ZA SKORZYSTANIE Z KALKURATORA")
        break

    wyrazenie = input("Rozwiąż wyrażenie: ")
    wynik = kalkulator_wyrazenia(wyrazenie)
    print("Wynik:", wyrazenie, "=", wynik)
    continue
