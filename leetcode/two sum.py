nums = [2,7,11,15]
target = 17


h = {}
for i, num in enumerate(nums):
    n = target - num
    if n not in h:
        h[num] = i
    else:
        print([h[n], i])
    print(h)


