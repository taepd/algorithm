from itertools import combinations

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]

for e in combinations(lst, m):
    print(*e)