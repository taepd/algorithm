
n = int(input())

arr = [int(input()) for _ in range(n)]

# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
arr.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n  # arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, n-1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))