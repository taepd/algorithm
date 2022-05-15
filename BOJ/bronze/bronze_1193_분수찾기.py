"""
대각선 합이 시그마k 의 형태이고, 홀수번째와 짝수번째 증가 방향이 반대인 패턴을 구현
"""


n = int(input())

arr = []
k = 0
while True:
    arr.append(k)
    if sum(arr) >= n:
        break
    k += 1
r = n - sum(arr[:k])

if k % 2 == 0:
    print(f'{r}/{k-r+1}')
else:
    print(f'{k-r+1}/{r}')
