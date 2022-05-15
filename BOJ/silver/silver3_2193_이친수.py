
# 실패: 시간 초과

# n = int(input())
#
# start = int(2**n)-1
# end = int(2**(n-1))
# cnt = 0
#
# for e in range(end, start):
#     if '11' in bin(e):
#         continue
#     else:
#       cnt += 1
#
# print(cnt)

# https://pro-jy.tistory.com/15

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n+1):
    if i < 3:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

