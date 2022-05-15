import sys
from collections import deque
from collections import defaultdict

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                tmp = list(set(graph[node]) - set(visited))
                queue.extend(sorted(tmp))

    return visited

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(len(bfs(graph, 1))-1)


# dfs가 더 연산이 빠른듯?

def dfs(v):
    visited[v] = 1
    for w in adj_lst[v]:
        if not visited[w]:
            dfs(w)


V = int(input())
E = int(input())
adj_lst = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)
visited = [0]*(V+1)
dfs(1)
print(sum(visited)-1)
