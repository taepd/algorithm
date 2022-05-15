# 효율성이 떨어짐

import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return False
    if [x, y] in arr:
        arr.remove([x, y])
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(input())

for __ in range(T):
    w, h, k = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(k)]
    cnt = 0
    while arr:
        if dfs(*arr[0]):
            cnt += 1
    print(cnt)



import sys
sys.setrecursionlimit(10 ** 5)

T = int(input())
def search(x,y):
  if x < 0 or x >= N or y < 0 or y >= M:
    return
  if G[x][y] == 0:
    return
  G[x][y]=0
  search(x+1,y)
  search(x,y+1)
  search(x-1,y)
  search(x,y-1)

input = sys.stdin.readline
for _ in range(T):
  M, N, K = map(int, input().split())
  G = [[0] * M for _ in range(N)]
  result = 0
  for _ in range(K):
    x, y = map(int,input().split())
    G[y][x] = 1
  for i in range(N):
    for j in range(M):
      if G[i][j] == 1:
        search(i, j)
        result += 1
  print(result)