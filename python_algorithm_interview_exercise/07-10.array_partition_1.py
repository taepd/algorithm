"""
n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
"""
nums = [1,4,3,2]
nums1 = [6,2,6,5,1,2]


# 오름차순 풀이
# 332ms

from typing import List


def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# 짝수 번째 값 계산
# 정렬을 하게 되면 결국 짝수 번째 값이 최솟값이므로 굳이 페어를 만들지 않아도 됨
# 308ms

def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum

# 파이썬다운 방식
# 슬라이싱 활용
# 284ms


def arrayPariSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


print(arrayPairSum(nums))
