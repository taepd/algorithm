# 1차 시도: 시간 초과
def solution(numbers):
    answer = []
    for n in numbers:
        m = 1
        while True:
            if sum(map(int, bin((n ^ (n+m)))[2:])) <= 2:
                answer.append(n+m)
                break
            else:
                m += 1
    return answer

# 2차 시도: numpy 배열을 이용한 미리 전체 배열 생성 -> 메모리 초과

# 3차 시도:  패턴을 파악해서 문자열로 처리

def solution(numbers):
    answer = []
    for n in numbers:
        tmp = bin(n)[2:]
        if '0' not in tmp:
            answer.append(int('10'+tmp[1:], 2))
        else:
            i = tmp.rfind('0')
            if len(tmp) == i+1:
                answer.append(int(tmp[:i]+'1', 2))
            else:
                answer.append(int(tmp[:i] + '10'+ tmp[i+2:], 2))
    return answer

