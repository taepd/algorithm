import sys

input = sys.stdin.readline
n = int(input())

point = [0]
for __ in range(n):
    point.append(int(input()))

dp = [0] * 301

if n >= 1:
    dp[1] = point[1]
if n >= 2:
    dp[2] = point[1] + point[2]
if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+point[i], point[i]+point[i-1]+dp[i-3])

print(dp[n])

