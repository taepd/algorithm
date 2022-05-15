import math
n = int(input())
arr = str(math.factorial(n))[::-1]
cnt = 0
for e in arr:
    if e == '0':
        cnt += 1
    else:
        break
print(cnt)