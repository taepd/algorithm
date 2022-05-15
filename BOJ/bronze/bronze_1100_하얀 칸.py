ans = 0

for i in range(8):
    for j, c in enumerate(input()):
        if i % 2 == 0 and j % 2 == 0 and c == 'F':
            ans += 1
        elif i % 2 != 0 and j % 2 != 0 and c == 'F':
            ans += 1

print(ans)


# step을 활용한 풀이
ans = 0

for i in range(8):
    row = input()
    for j in range(i % 2, 8, 2):
        if row[j] == 'F':
            ans += 1

print(ans)