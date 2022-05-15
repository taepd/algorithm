list = list("┌┬┐├┼┤└┴┘")

print(list)

uni_list = [ord(c) for c in list]
print(uni_list)

for i, ord in enumerate(uni_list):
    print(chr(ord), end="")
    if i%3 == 2:
        print()


