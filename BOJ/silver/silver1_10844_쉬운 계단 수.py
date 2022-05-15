
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

print(sum(dp[n]) % 1000000000)