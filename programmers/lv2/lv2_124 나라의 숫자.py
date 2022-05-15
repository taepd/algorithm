"""
문제 설명
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1	1	6	14
2	2	7	21
3	4	8	22
4	11	9	24
5	12	10	41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.
입출력 예
n	result
1	1
2	2
3	4
4	11
"""

"""
재귀를 이용한 3진법 변환
일반적인 3진법과 다르게 0이 없고 1부터 시작하므로, n-1(재귀함수들도) 해줘야 함
"""

def solution(n):
    return n_ary(n-1, 3)

t = '124'
def n_ary(number, base):
    q, r = divmod(number, 3)
    n = t[r]
    return n_ary(q-1, base) + n if q else n


"""
문자열을 이용한 풀이
"""

def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1  # num 리스트 인덱스를 맞추기 위해
        answer = num[n % 3] + answer
        n //= 3

    return answer

"""
재귀를 이용한 풀이
"""

def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]

