'''
result[i]의 최댓값을 구하는 것은 세 가지 방법에 의해 결정된다.

1) OXOO: 연속 두 개
2) OXO: 하나 띄고 한 개
3) X: i번째를 마시지 않는 경우
'''

import sys

input = sys.stdin.readline

def sol2156():
    n = int(input())
    arr = [0]
    dp = [0] * (n+1)
    for __ in range(n):
        arr.append(int(input()))

    for i in range(1, len(arr)):
        if i < 3:
            dp[i] = sum(arr[:i+1])
        else:
            dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])
    print(max(dp))

sol2156()