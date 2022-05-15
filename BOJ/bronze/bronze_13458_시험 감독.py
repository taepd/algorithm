import sys

input = sys.stdin.readline

n = int(input())

class_arr = list(map(int, input().split()))

m, s = map(int, input().split())

ans = 0
for e in class_arr:
    e -= m
    ans += 1
    if e > 0:
        ans += (e-1)//s + 1
print(ans)
