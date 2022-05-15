"""
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
abcde	c
qwer	we
"""

s = 'abcde'

def solution(s):
    q, r = divmod(len(s), 2)
    return s[q] if r != 0 else s[q-1:q+1]


print(solution(s))

"""
간결 풀이
"""

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]