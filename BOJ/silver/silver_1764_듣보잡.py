import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a, b= set(), set()

for __ in range(N):
    a.add(input().rstrip())
for __ in range(M):
    b.add(input().rstrip())

ans = sorted(list(a & b))

print(len(ans))
for e in ans:
    print(e)