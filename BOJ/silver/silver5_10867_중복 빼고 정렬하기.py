import sys

input = sys.stdin.readline

n = int(input())

arr = list(set(map(int, input().split())))

print(' '.join(map(str, sorted(arr))))


# short code

input()
print(*sorted(set(map(int, input().split()))))