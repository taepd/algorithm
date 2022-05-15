"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
예제1
- 입력
" A man, a plan, a canal: Panama"
- 출력
true

예제2
- 입력
"race a car"
- 출력
false
"""


s = "A man, a plan, a canal: Panama"
s2 = "race a car"

# 리스트를 이용한 풀이, 304ms
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # isalnum() : 영문자, 숫자 여부를 판별하는 함수
            strs.append(char.lower())
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True



# 데크를 이용한 풀이
import collections
from typing import Deque  # 타입 힌트를 주기 위해


def isPalindrome(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 슬라이싱을 이용한 풀이
import re  # 정규표현식

def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱

print(isPalindrome(s))


