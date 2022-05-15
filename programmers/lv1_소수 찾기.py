"""
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""

"""
'에라토스테네스의 체' 이용한 풀이
"""
import timeit

start_time = timeit.default_timer() # 시작 시간 체크

n = 30000000
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            # num -= set(range(2*i, n+1, i))  # i를 훑으면서 그 전값까지 처리가 다 되므로 i*i도 가능
    return len(num)


print(solution(n))

terminate_time = timeit.default_timer() # 종료 시간 체크

print("%f초." % (terminate_time - start_time))

