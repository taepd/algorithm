
plain = [[0]*100 for __ in range(100)]
arr = [list(map(int, input().split())) for __ in range(4)]

for lst in arr:
    a, b, c, d = lst
    for x in range(a, c):
        for y in range(b, d):
            plain[x][y] = 1

print(sum([sum(e) for e in plain]))
