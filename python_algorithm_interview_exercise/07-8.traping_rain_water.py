"""
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]

# 투 포인터를 최대로 이동
# O(n). 52ms
from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1  # 포인터 세팅
    left_max, right_max = height[left], height[right] # 최대높이 초기화

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


# 스택 쌓기
def trap(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우(가장 마지막 스택값보다 높아진 경우)
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            # distance = i - top
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume

print(trap(height))
# print(trap(height2))

