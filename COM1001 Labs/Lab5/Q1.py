# I think this one can be done in a number of ways. This is just the one I came up with. I assume it would be pretty unefficient against big lists.
# Also I didn't define this as a function but you can try to implement it as an exercise.

infile = open("Q1 input.txt","r")

dct = {}

for i in infile:
    Lst = i.strip().split(":")
    Lst2 = Lst[1].split(",")
    dct[Lst[0]] = Lst2

wanted = input()
found = False

for i in dct:
    if (wanted == i) or (wanted in dct[i]):
        print("{" + f"'{i}': {dct[i]}" + "}")
        found = True
        break

if not found:
    print("WARNING")