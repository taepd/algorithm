"""
문제 설명
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	수박수
4	수박수박
"""
import timeit

start_time = timeit.default_timer() # 시작 시간 체크

n = 10000000
"""
list 생성 후 join까지 하기 때문에 효율성 떨어짐
"""
def solution(n):
    return ''.join(['수' if i % 2 == 0 else '박' for i in range(n)])

"""
best 풀이
"""
def solution(n):
  return "수박"*(n//2) + "수"*(n%2)

print(solution(n))

terminate_time = timeit.default_timer() # 종료 시간 체크

print("%f초." % (terminate_time - start_time))