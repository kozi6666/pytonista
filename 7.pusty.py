lsit = []

for x in range(1, 30):
    if x % 2 == 0 and x % 3 == 0:
        print("fizzbuzz")
    elif x % 2 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        lsit.append(x)

print("Liczby pierwsze: ", lsit)
