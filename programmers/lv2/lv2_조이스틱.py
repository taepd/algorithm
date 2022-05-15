def solution(name):
    answer = 0
    i = 0
    arr = list(name)
    while True:
        r = ord(arr[i]) - ord('A')
        if r // 14:
            answer += 12 - r % 14
        else:
            answer += r
        arr[i] = 'A'

        if arr.count('A') == len(name):
            return answer

        left, right = 1, 1
        while arr[i - left] == 'A':
            left += 1
        while arr[i + right] == 'A':
            right += 1
        answer += left if left < right else right
        i += -left if left < right else right

    return answer

name = "JEROEN"  # 56

print(solution(name))