# import sys
#
# n = int(sys.stdin.readline())
#
# dp = [[],[],[]] * (n+1)
#
# for i in range(1, n+1):
#     if i == 1:
#         dp[1] = list(map(int, input().split()))
#     else:
#         dp[i] = list(map(int, input().split()))
#         for j in range(3):
#             dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
#
# print(min(dp[n]))

# 개선한 풀이

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0, 0, 0]

for e in arr:
    dp = [e[0] + min(dp[1], dp[2]), e[1] + min(dp[0], dp[2]), e[2] + min(dp[0], dp[1])]

print(min(dp))


# 간결한 풀이

moneys = [list(map(int, money.split())) for money in [*open(0)][1:]]
M = [0,0,0]
for money in moneys:
    M = [money[0] + min(M[1:]), money[1] + min(M[0], M[-1]), money[2] + min(M[:-1])]
print(min(M))