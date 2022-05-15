arr = [(int(input()), i) for i in range(8)]

arr.sort(reverse=True)

print(sum(e[0] for e in arr[:5]))
print(' '.join(map(str, sorted([e[1]+1 for e in arr[:5]]))))

