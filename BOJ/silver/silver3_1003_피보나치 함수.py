#
# fibo = [0] * 41
# dp = [[0, 0]] * 41
#
# def fibonacci(n):
#     if n == 0:
#         dp[n] = [1, 0]
#         fibo[n] = 0
#         return 0
#     elif n == 1:
#         dp[n] = [0, 1]
#         fibo[n] = 1
#         return 1
#     else:
#         dp[n] = [sum(x) for x in zip(dp[n-1], dp[n-2])]
#         fibo[n] = fibo[n-1] + fibo[n-2]
#         return fibo[n]
#
# for i in range(41):
#     fibonacci(i)
#
#
# for _ in range(int(input())):
#     n = int(input())
#     print(*dp[n])


"""
정리한 풀이
효율성을 위해 input을 sys.stdin.readline으로, dp의 불필요한 연산 제거
"""

import sys

input = sys.stdin.readline

dp = [[0, 0]] * 41
dp[0], dp[1] = [1, 0], [0, 1]

for i in range(2, 41):
    dp[i] = [sum(x) for x in zip(dp[i-1], dp[i-2])]

for _ in range(int(input())):
    n = int(input())
    print(*dp[n])

