from itertools import combinations

ans = float('inf')
n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]

combo = list(combinations([i for i in range(n)], n//2))

start, link = combo[:len(combo)//2], combo[len(combo)//2:][::-1]

for s, l in zip(start, link):
    sum_s, sum_l = 0, 0
    for i, j in combinations(s, 2):
        sum_s += arr[i][j] + arr[j][i]
    for i, j in combinations(l, 2):
        sum_l += arr[i][j] + arr[j][i]
    ans = min(abs(sum_s-sum_l), ans)

print(ans)
