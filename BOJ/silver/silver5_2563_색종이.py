
n = int(input())

arr = [list(map(int, input().split())) for __ in range(n)]

plain = [[0] * 100 for __ in range(100)]
cnt = 0

for e in arr:
    w, h = e[0], e[1]
    for i in range(w-1, w+9):
        for j in range(h-1, h+9):
            if plain[i][j] == 0:
                plain[i][j] = 1
                cnt += 1

print(cnt)