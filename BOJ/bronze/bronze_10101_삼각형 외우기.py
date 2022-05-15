lst = []
for __ in range(3):
    lst.append(int(input()))

if sum(lst) == 180:
    a, b, c = lst
    if a == b == c:
        print('Equilateral')
    elif a != b != c != a:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')