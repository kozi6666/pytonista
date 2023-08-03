tasks = ["dupa", "cipa"]


def show():
    print("")
    print("Twoje zadania: ")
    task_index = 0

    for task in tasks:
        print(str(task_index) + "." + f"{task}")
        task_index += 1


def add():
    print("")
    new_task = input("Podaj zadanie, któro chcesz dodać: ")

    if new_task in tasks:
        print("to zadanie juz jest na liscie")
    else:
        tasks.append(new_task)
        print("Zadanie zostało dodane: " f"{new_task}")


def out():
    show()
    task_out = int(input("podaj index zadania któro chcesz usunąć"))

    if len(tasks) > task_out >= 0:
        tasks.pop(task_out)
        for _ in tasks:
            print("Zadanie " + f"{task_out}" + "." + " Usunięte")
    else:
        print("Nie ma takiego zadania")


def menu():
    while True:

        print("")
        print("Witaj w programie ToDo")
        print("")
        print("")
        print("1.Pokaż listę")
        print("2.Dodaj zadanie")
        print("3.Usuń zadanie")
        print("4.Wyjdź")
        print("")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            show()
            continue
        elif choice == "2":
            add()
            continue
        elif choice == "3":
            out()
            continue
        elif choice == "4":
            print("4")
            break
        else:
            print("Nie ma takiej opcji.")
            continue


menu()
