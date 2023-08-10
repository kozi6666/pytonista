# with open("kuba.txt", "w") as file:
#     txt = file.write("Dupa\ndupa\ndupa\ndupa")

# with open("kuba.txt", "a") as file:
#     file.write("Dupa")

def otworz(x):
    with open(x, "r") as file:
        print(file.readlines())
    # print(im)


#
#     for element in file:
#         print (tuple(element.replace("\n", "").split(" ")))

# tex = [1, 2, 3, 4, 1, 2, 7]
#
# # x = (set(tex))
# # print(list(x))
#
# print(list(set(tex)))
def interface():
    while True:

        print("")
        print("")
        print("otworz plik ")
        print("")
        print("")

        choice = input("...")

        otworz(choice)
        continue

#
interface()
