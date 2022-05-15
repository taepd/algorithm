def solution(s):
    stack = []
    for e in s:
        if not stack:
            stack.append(e)
        else:
            if stack[-1] == e:
                stack.pop()
            else:
                stack.append(e)
    if stack:
        return 0
    else:
        return 1