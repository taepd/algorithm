import math
n = int(input())

for __ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    rsum = r1+r2
    if d == 0 and r1 == r2:
        print(-1)
    elif rsum > d:
        if max(r1, r2) == d + min(r1, r2):
            print(1)
        elif max(r1, r2) > d + min(r1, r2):
            print(0)
        else:
            print(2)
    elif rsum == d:
        print(1)
    else:
        print(0)

