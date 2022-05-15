
s = '02984'

def solution(s):
    answer = int(s[0])
    s = list(map(int, s))
    for n in s:
        if answer <= 1 or n <=1:
            answer += n
        elif n == 1:
            answer += 1
        else:
            answer *= n
    return answer

print(solution(s))