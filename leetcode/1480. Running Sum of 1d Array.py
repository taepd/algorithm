"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

from typing import List
from functools import reduce

nums = [1,2,3,4]

# reduce 활용
# 152 ms
def runningSum(nums: List[int]) -> List[int]:
    return [reduce(lambda x, y: x + y, nums[:i + 1]) for i in range(len(nums))]

# for문 활용. 기본형태
# 효율면에서 이게 낫다
# 36 ms
def runningSum(nums: List[int]) -> List[int]:
    result = []
    sum = 0
    for num in nums:
        sum += num
        result.append(sum)
    return result

# 미리 배열 생성하기
# 40ms
# append보다 미리 생성한 배열이 효율이 좋은 걸로 알고 있었는데 꼭 그렇지도 않은가 봄
def runningSum(nums: List[int]) -> List[int]:
    result = [0 for _ in nums]  # nums 길이만큼 zero_list 생성

    sum = 0
    for i, num in enumerate(nums):
        sum += num
        result[i] = sum
    return result

# leet recommend
# accumulate 활용
# iterrools.accumulate가 정확히 본 문제의 역할을 함
# 40ms

from itertools import accumulate

def runningSum(nums: List[int]) -> List[int]:
    return accumulate(nums)

print(runningSum(nums))



