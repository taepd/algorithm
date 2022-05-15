n, k = map(int, input().split())

arr = [list(map(int, input().split())) for __ in range(n)]

tgt = [e for e in arr if e[0] == k][0]

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

cnt = 0
for e in arr:
    if e[1] == tgt[1] and e[2] == tgt[2] and e[3] == tgt[3]:
        break
    cnt += 1

print(cnt+1)
