"""
문자열을 뒤집는 함수는 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
<예제 1>
- 입력
["h", "e", "l", "l", "o"]
- 출력
["o", "l", "l", "e", "h"]
"""

s = ["h", "e", "l", "l", "o"]

# 투 포인터를 이용한 스왑
from typing import List

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

reverseString(s)
print(s)

# 파이썬다운 방식
from typing import List


def reverseString(s: List[str]) -> None:
    s.reverse()

reverseString(s)
print(s)

# 슬라이싱 이용 방식
s = s[::-1]

print(s)
# 위가 안될 경우(공간 복잡도가 O(1)로 제한될 경우)
s[:] = s[::-1]

print(s)

