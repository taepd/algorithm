# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = list(map(int, input().split()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[j]+1, dp[i])
#
# print(max(dp))


# 이진분류를 이용한 방법
# import bisect
#
# x = int(input())
# arr = list(map(int, input().split()))
#
# dp = [arr[0]]
# a =0
# for i in range(x):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect.bisect_left(dp, arr[i])
#         dp[idx] = arr[i]
#
# print(len(dp))


# 결국 더 작은 수가 나오면 그 수를 앞쪽의 적절한 위치의 값과 교체시키는 전략
import sys

input = sys.stdin.readline


def sol11053():
    n = int(input())

    seq = list(map(int, input().split()))

    lis = [seq[0]]
    for num in seq[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            for i in range(len(lis)):
                if lis[i] >= num:
                    lis[i] = num
                    break
    print(len(lis))


if __name__ == '__main__':
    sol11053()

