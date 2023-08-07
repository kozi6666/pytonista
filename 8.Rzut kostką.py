import random

list = [1, 2, 3, 4, 5, 6]
x = 1
nums = []
suming = sum(nums)
while suming <= 21:
    req = input("...")
    if req == "":
        print(f"{x}"" Rzut kostką")
        print("")
        num = (random.choice(list))
        print(num)
        nums.append(num)
        x += 1
        suming = sum(nums)
        print(suming)

        continue
    elif req == "q":
        break
    else:
        continue
