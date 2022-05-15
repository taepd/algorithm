
try:
    while input():
        arr = list(map(int, input().split()))
        print(arr)
except EOFError:
    exit()
