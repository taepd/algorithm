
n = int(input())
arr = [64]

while sum(arr) > n:
    t = arr.pop()//2
    arr.append(t)
    if sum(arr) < n:
        arr.append(t)

print(len(arr))


# 이진법 변환 후 1만 계산
a=int(input())
print(str(bin(a)).count('1'))