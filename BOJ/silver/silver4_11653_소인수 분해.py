# n = int(input())
#
# d = 2
# while n != 1:
#     if n % d == 0:
#         n /= d
#         print(d)
#     else:
#         d += 1


# 불필요한 순회를 최소화한 풀이
import sys

def f(N):

    for i in range(2,int(N**0.5+1)):
        if N % i == 0:
            print(i)
            return i
    return print(N)

input = sys.stdin.readline
N = int(input())
while(N != 1):
    try:
        N //= f(N)
    except:
        break
