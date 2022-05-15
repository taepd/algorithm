a, b = map(int, input().split())
list = [[0 for _ in range(b)] for _ in range(a)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            list[x - 1][y - 1 + j] = 1
        else:
            list[x - 1 + j][y - 1] = 1

for row in list:
    for e in row:
        print(e, end=' ')
    print()

