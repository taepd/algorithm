
n = int(input())

for i in range(1, n+1):
    if i == n:
        print('*'*(2*i-1))
        continue
    for j in range(n-i, 0, -1):
        print(' ', end='')
    for j in range(2*i-1):
        if j == 0 or j == 2*i-2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

