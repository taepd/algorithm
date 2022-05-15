
# n = int(input())
#
# dp = [0] * 81
#
# def fiv(n):
#     if n == 1 or n == 2:
#         dp[n] = 1
#     else:
#         dp[n] = dp[n-1] + dp[n-2]
#     return dp[n]
#
# for i in range(3, n+1):
#     fiv(i)
#
# print((dp[n]*2+dp[n-1])*2)


# version2
# 매 for문마다 불필요하게 if문을 거치는 것을 제거

n = int(input())

dp = [0] * 81

dp[1], dp[2] = 1, 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print((dp[n]*2+dp[n-1])*2)
