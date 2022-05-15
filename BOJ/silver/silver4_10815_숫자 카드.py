input()
n_set = set(map(int, list(input().split())))
input()
arr = list(map(int, input().split()))

for e in arr:
    if set([e]) - n_set:
        print(0, end=' ')
    else:
        print(1, end=' ')

# 그냥 간단하게 if in 문으로

import sys
input = sys.stdin.readline

input()
arr1 = set(input().split())
input()
arr2 = input().split()
ans = ""
for e in arr2:
    if e in arr1:
        ans +="1 "
    else:
        ans +='0 '
print(ans)