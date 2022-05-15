from collections import Counter

s = Counter(input())

for i in range(ord('a'), ord('z')+1):
    print(s[chr(i)], end=' ')