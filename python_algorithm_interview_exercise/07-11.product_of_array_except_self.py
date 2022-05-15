"""
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""
nums = [1,2,3,4]

# 제약사항에 O(n)이 있으므로, 이중 for문은 안됨
# 결국 자기 자신을 제외한 왼쪽의 곱과, 오른쪽의 곱을 따로 구해서 곱해주는 전략
from functools import reduce
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]
        print(p)
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


# timeout 걸림
def productExceptSelf(nums: List[int]) -> List[int]:
    return [reduce(lambda x, y: x * y, (nums[:i]+nums[i+1:])) for i in range(len(nums))]



print(productExceptSelf(nums))
