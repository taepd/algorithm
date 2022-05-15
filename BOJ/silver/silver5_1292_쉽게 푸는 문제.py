
s, e = map(int, input().split())

cnt = 1
arr = []
while e >= len(arr):
    arr += [cnt] * cnt
    cnt += 1

print(sum(arr[s-1:e]))

