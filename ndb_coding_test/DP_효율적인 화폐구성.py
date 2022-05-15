
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받기
units = [int(input()) for _ in range(n)]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for k in units:
    for i in range(k, m + 1):
        if d[i - k] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[i] = min(d[i], d[i - k] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

