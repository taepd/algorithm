def solution(scores):
    answer = ''
    # scores = list(map(list, zip(*scores)))
    for i, v in enumerate(zip(*scores)):
        myself = v[i]
        if (myself == max(v) or myself == min(v)) and v.count(myself) == 1:
            answer += get_grade((sum(v)-myself)/(len(v)-1))
        else:
            answer += get_grade(sum(v)/len(v))
    return answer

def get_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 50: return 'D'
    else: return 'F'