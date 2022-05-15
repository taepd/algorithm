from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

combo = list(combinations(dwarfs, 7))

for c in combo:
    if 100 == sum(c):
        for e in sorted(c):
            print(e)
        break
