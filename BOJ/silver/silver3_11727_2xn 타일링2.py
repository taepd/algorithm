'''
n-1, n-2의 조합 수에 덧붙여 나오는 가짓수를 계산
이 때, 중복되는 경우 (세로 블록이 연달아 채워지는 경우 등)을 제외하기 위해 dp[i-2] * 3 이 아닌 2를 해줌
'''

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    else:
        dp[i] = (dp[i-2]*2) + dp[i-1]

print(dp[n] % 10007)