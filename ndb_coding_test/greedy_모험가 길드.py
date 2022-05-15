
n = [2, 3, 1, 2, 2]

def solution(n):
    answer = 0
    cnt = 0
    for e in n:
        cnt +=1
        if cnt >= e:
            answer +=1
            cnt = 0
    return answer

print(solution(n))