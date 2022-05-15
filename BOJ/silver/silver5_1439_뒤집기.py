
s = input()

arr = []
tmp = []
for e in s:
    if not tmp:
        tmp.append(e)
    else:
        if tmp[-1] == e:
            tmp.append(e)
        else:
            arr.append(tmp)
            tmp = [e]
arr.append(tmp)

print(len(arr)//2)


# 0이나 1이 토글될 때 count를 올리는 전략
S = input()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count + 1) // 2)