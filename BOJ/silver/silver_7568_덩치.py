arr = [list(map(int, input().split())) for _ in range(int(input()))]

ans = []
for e1 in arr:
    x1, y1 = e1
    cnt = 1
    for e2 in arr:
        x2, y2 = e2
        if x2 > x1 and y2 > y1:
            cnt += 1
    ans.append(cnt)

print(*ans)

