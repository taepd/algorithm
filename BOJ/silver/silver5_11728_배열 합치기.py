import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(' '.join(map(str, sorted(arr1+arr2))))