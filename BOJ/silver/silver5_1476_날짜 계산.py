
e, s, m = map(int, input().split())

while True:
    if e == s and s == m:
        print(e)
        break
    mn = min(e, s, m)
    if mn == e:
        e += 15
    elif mn == s:
        s += 28
    else:
        m += 19



# 이런 풀이도 가능
E, S, M = map(int, input().split())
year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1