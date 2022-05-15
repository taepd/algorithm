# two point 전략

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
rp = 0
current_sum = 0


for lp in arr:
    while current_sum < m and rp < n:
        current_sum += arr[rp]
        rp += 1
    if current_sum == m:
        cnt += 1
    current_sum -= lp

print(cnt)

