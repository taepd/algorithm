def solution(s):
    answer = []
    for e in s:

        i = e.find('110')
        trg = e.find('111')
        while '111' in e[:i + 2]:
            e = e[:i] + e[i + 2:]  # 0111110
            e[:trg] + '110' + e[trg:]
    return answer