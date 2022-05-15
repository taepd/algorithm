
n = int(input())

plain = {}

for i in range(n):
    a, b, c, d = map(int, input().split())
    for x in range(b, b+d):
        for y in range(a, a+c):
            plain[(x,y)] = i

for i in range(n):
    cnt = 0
    for v in plain.values():
        if v == i:
            cnt += 1
    print(cnt)
