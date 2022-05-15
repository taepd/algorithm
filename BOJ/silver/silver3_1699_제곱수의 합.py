"""
greedy 전략
1차 반례 41 = 5^2+4^2 이 6^2+2^2+1 보다 최소항

"""

# n = int(input())
# cnt = float('inf')
# for i in range(int(n**0.5), 0, -1):
#     _n = n
#     m = i
#     temp = 0
#     while True:
#         if m > 1:
#             _n -= m**2
#             temp += 1
#         else:
#             temp += _n
#             break
#         if _n < m**2:
#             m = int(_n ** 0.5)
#     cnt = min(cnt, temp)
#
# print(cnt)


# 시간 초과  ** 연산이 시간효율성에서 떨어짐
# n = int(input())
#
# dp = [i for i in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, int(i ** 0.5) + 1):
#         tmp = dp[i - j ** 2] + 1
#         if dp[i] > tmp:
#             dp[i] = tmp
#
# print(dp[n])

n = int(input())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if i < j * j:
            break
        tmp = dp[i - j * j] + 1
        if dp[i] > tmp:
            dp[i] = tmp

print(dp[n])
