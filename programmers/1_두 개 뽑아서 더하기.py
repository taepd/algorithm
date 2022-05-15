"""
두 개 뽑아서 더하기
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
입출력 예
numbers	result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
입출력 예 설명
입출력 예 #1

2 = 1 + 1 입니다. (1이 numbers에 두 개 있습니다.)
3 = 2 + 1 입니다.
4 = 1 + 3 입니다.
5 = 1 + 4 = 2 + 3 입니다.
6 = 2 + 4 입니다.
7 = 3 + 4 입니다.
따라서 [2,3,4,5,6,7] 을 return 해야 합니다.
입출력 예 #2

2 = 0 + 2 입니다.
5 = 5 + 0 입니다.
7 = 0 + 7 = 5 + 2 입니다.
9 = 2 + 7 입니다.
12 = 5 + 7 입니다.
따라서 [2,5,7,9,12] 를 return 해야 합니다.
"""

numbers = [2, 1, 3, 4, 1]
# result = [2, 3, 4, 5, 6, 7]

"""
- 1차 시도 
enumerate와 list comprehension 사용
서로 같은 index가 아닐 경우라는 조건을 그대로 if문으로 옮김

"""
# def solution(numbers):
#     answer = list(set(i + j for index_j, j in enumerate(numbers)
#                       for index_i, i in enumerate(numbers)
#                       if index_i != index_j))
#     answer = sorted(answer)  # 정렬이 오름차순으로 안되는 경우가 있으므로 정렬을 거쳐야 함
#     return answer


"""
- 2차 시도
range(len())을 이용한 index 직접 활용
return을 바로 하고 정렬 또한 바로 적용하여 코드를 축약하였음 
"""

# def solution(numbers):
#     return sorted(list(set(numbers[i] + numbers[j] for j in range(len(numbers))
#                       for i in range(len(numbers))
#                       if i != j)))

"""
- 3차 시도
하나의 리스트에서 combination을 구할 때, 안쪽 for문에서 바깥쪽 for문의 index+1을 해주면 됨
"""


# def solution(numbers):
#     return sorted(list(set(numbers[i] + numbers[j] for i in range(len(numbers))
#                            for j in range(i + 1, len(numbers)))))

"""
- 4차 시도
혹은 if문을 줘서 i<j로 하면 됨
"""

def solution(numbers):
    return sorted(list(set(numbers[i] + numbers[j] for i in range(len(numbers))
                           for j in range(len(numbers)) if i < j)))


print(solution(numbers))
