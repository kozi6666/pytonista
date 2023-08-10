def interface():
    while True:

        print("")
        print("1.Wczytaj wiadomość")
        print("2.Dodaj wiadomość")
        print("3.Wyjdź")
        print("")

        choice = input("...")

        if choice == "1":
            print("1.Wczytaj wiadomość")
            get_text()
            continue
        elif choice == "2":
            sends = input("2.Dodaj wiadomość: ")
            send(sends)
            continue
        elif choice == "3":
            print("3.Wyjdź")
            break
        else:
            print("Nie ma takiej opcji.")
            continue


def get_text():
    with open("9.messanger.txt", "r") as file:
        msg = file.read()
        print(msg)


def send(sends):
    with open("9.messanger.txt", "w") as file:
        file.write(sends)


interface()
