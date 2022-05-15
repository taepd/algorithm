import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for __ in range(n)]
l = len(arr)
mx = 0
for e, k in sorted(Counter(arr).items(), key=lambda x: x[0]):
    tmp = e * l
    if mx < tmp:
        mx = tmp
    l -= k
print(mx)