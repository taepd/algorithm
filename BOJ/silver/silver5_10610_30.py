# 30의 배수: 30의 소인수분해 2*3*5
# 1의 자리는 0이어야 함 <- 10의 배수
# 3의 배수는 각 자릿수의 합이 3의 배수이면 전체가 3의 배수

n = int(input())  # 102

arr = list(map(int, str(n)))  # [1, 0, 2]

if sum(arr) % 3 == 0 and str(n).find('0') != -1:
    arr.sort(reverse=True)  # [2, 1, 0]
    print(''.join(map(str, arr)))  # 210
else:
    print(-1)


# 최적화 풀이

N = sorted(input(), reverse=True)

if '0' not in N or sum(map(int,N))% 3 != 0:
    print(-1)
else:
    print(''.join(N))
