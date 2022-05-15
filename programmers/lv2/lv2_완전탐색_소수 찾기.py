"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""
"""
set을 활용한 에라토스테네스의 체 전략
따로 수 배열을 만들어서 빼지 않는 대신, 최댓값의 제곱근까지 모든 i를 순회
그럼에도 속도, 메모리 모두 아래 풀이보다 낫다
"""

from itertools import permutations

def solution(numbers):
    arr = set()
    for i in range(1, len(numbers)+1):
        for e in permutations(numbers, i):
            n = ''
            for f in list(e):
                n +=f
            arr.add(int(n))
    arr -= set(range(2))
    mx = max(arr)
    for i in range(2, int(mx**0.5)+1):
        arr -= set(range(i*2, mx+1, i))

    return len(arr)



"""
에라토스테네스의 체를 이용하는 기본적 방법
위 방법보다 효율이 떨어진다
"""

from itertools import permutations

def solution(numbers):
    arr = set()
    for i in range(1, len(numbers)+1):
        for e in permutations(numbers, i):
            n = ''
            for f in list(e):
                n +=f
            arr.add(int(n))
    mx = max(arr)
    p_list = [i for i in range(2, mx+1)]
    for i in range(2, int(mx**0.5)+1):
        if i in p_list:
            arr -= set(range(i*2, mx+1, i))
    cnt = 0
    for e in arr:
        if e in p_list:
            cnt += 1

    return cnt

    return len(arr)