"""
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
입출력 예
n	result
45	7
125	229
입출력 예 설명
입출력 예 #1

답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
45	1200	0021	7
따라서 7을 return 해야 합니다.
입출력 예 #2

답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
125	11122	22111	229
따라서 229를 return 해야 합니다.
"""

n = 45

def solution(n):
    list = []

    decimal_to_ternary(n, list)
    return ternary_to_decimal(list)

def decimal_to_ternary(n, list):
    if n == 0:
        return
    list.append(n % 3)
    n //= 3

    decimal_to_ternary(n, list)

def ternary_to_decimal(list):
    list.reverse()
    sum = 0
    for i in range(len(list)):
        sum += list[i]*(3**i)
    return sum


"""
풀이 1
"""

def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3

    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer

"""
풀이 2
"""

def n_ary(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(r)
    return ''.join(map(str, reversed(result)))

def solution(n):
    b3 = n_ary(n, 3)
    b3 = b3[::-1]
    return int(b3, 3)  # 쉬운 10진법 변환


print(solution(n))

