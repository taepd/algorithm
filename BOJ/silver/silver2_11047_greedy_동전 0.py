n, k = map(int, input().split())

unit_arr = [int(input()) for _ in range(n)]

unit_arr.sort(reverse=True)

ans = 0

for unit in unit_arr:
    if k >= unit:
        ans += k // unit
        k = k % unit

print(ans)
