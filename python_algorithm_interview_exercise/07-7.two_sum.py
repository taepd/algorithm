"""
덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = [2,7,11,15]
target = 9


# brute force로 계산
# 모든 경우의 수를 다 비교. 비효율적.
# O(n^2). 실행 속도 5,284ms
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# in을 이용한 탐색
# 전부 비교하지 않고 target-n값이 존재하는지만 탐색
# O(n^2)이지만 파이썬 내부함수 in이 for문 비교보다 더 효율적
# 900ms

def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            # return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]  # 책 방식
            return [nums.index(n), nums.index(complement)]


# 첫 번째 수를 뺀 결과 키 조회
# 수를 키로, 인덱스를 값으로 하는 hash table로 만듬
# 평균적으로 O(1), 최악의 경우 O(n). 48ms
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:  # 후건은 동일 숫자합일 경우 자신은 제외하기 위해(페어를 만들어야 하므로)
            return [i, nums_map[target - num]]

# 조회 구조 개선
# 모두 해시 테이블로 저장하지 않고 정답을 찾게 되면 바로 return가능
# 성능은 비슷하나 코드가 간결해짐
# 44ms
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 `for`문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투 포인터 이용
# input list가 정렬되있다고 가정했을 때 가능. 해당 문제에선 적용 불가능.
# 두 포인터의 합이 target보다 크면 오른쪽 포인터가 왼쪽으로 이동, 작으면 왼쪽 포인터가 오른쪽으로 이동하는 방식
# O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

print(twoSum(nums, target))

# 고(Go)를 이용한 구현
# 3번의 hash table을 이용한 알고리즘과 동일하지만, 보다 최적화된 언어라서 월등히 빠름
# 경우에 따라서는 성능을 위해 다양한 언어로 구현하는 것이 강점이 될 수 있음
# 8ms
# func twoSum(nums []int, target int) []int {
#     numsMap := make(map[int]int)
#
#     // 키와 값을 바꿔서 딕셔너리로 저장
#     for i, num := range nums {
#         numsMap[num] = i
#     }
#
#     // 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#     for i, num := range nums {
#         if j, ok := numsMap[target-num]; ok && i != j {
#             return []int{i, j}
#         }
#     }
#
#     return []int{}
# }





