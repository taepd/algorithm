
n = int(input())
timer = [300, 60, 10]
ans = []

for i, t in enumerate(timer):
    ans.append(n // t)
    n %= t
print(-1) if n else print(*ans)

