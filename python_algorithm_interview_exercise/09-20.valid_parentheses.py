"""
괄호로 된 입력값이 올바른지 판별하라.
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""

s = "()[]{}"

# 스택 일치 여부 판별
# 파이썬 리스트는 스택 연산(push, pop)이 O(1)이므로 그대로 사용해도 무방
# 매칭 테이블을 만들어서 활용

def isValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:  # 매핑 테이블에 존재하지 않는 문자는 모두 스택에 푸쉬
            stack.append(char)
        elif not stack or table[char] != stack.pop():  # not stack: 비정상 케이스(None)등에 대한 예외처리
            return False
    return len(stack) == 0

print(isValid(s))



