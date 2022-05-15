

cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    print(f'Case {cnt}: {(v//p)*l + min(l, (v-(v//p)*p))}')
    cnt += 1
