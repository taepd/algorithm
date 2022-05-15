"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	6210
[3, 30, 34, 5, 9]	9534330
[40, 403] 40403
[0, 0, 0, 0, 0] 0
[21, 212] 21221
"""

"""
1~6 테스트 케이스 실패하는데, 반례를 찾지 못함

가장 큰 수의 길이만큼 특정 수를 그 수의 첫 번째 수로 채워넣은 뒤, 이를 원래 수와 리스트 형식으로
짝지어주고, 이를 활용해 다중 우선순위 정렬 후, 원래 수를 추출하는 전략
"""
def solution(numbers):
    list = [[str(n)] for i, n in enumerate(numbers)]
    m = len(str(max(numbers)))

    for s in list:
        s.append(s[0].ljust(m, s[0][0]))
    print(list)
    sorted_list = sorted(list, key=lambda x: (x[1], x[0]), reverse=True)

    return str(int(''.join([s[0] for s in sorted_list])))


"""
내가 생각한 것의 간결 명쾌한 버전..
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))