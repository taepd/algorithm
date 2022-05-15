"""
가장 긴 팰린드롬 부분 문자열을 출력하라.
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

# 짝수/홀수 두 개의 투 포인터를 좌측부터 우측으로 진행하며 팰린드롬을 확인해나가는 전략

def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),  # 짝수 투 포인터
                     expand(i, i + 2),  # 홀수 투 포인터터
                     key=len)
    return result


