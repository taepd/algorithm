
t = int(input())

dp = [0, 1, 1, 1, 2, 2]
dp += [0] * 95

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(t):
    n = int(input())
    print(dp[n])