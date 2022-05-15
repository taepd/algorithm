n = int(input())

odds = '* '*(n//2+n%2)
even = ' *'*(n//2)
for i in range(n):
    print(odds)
    print(even)