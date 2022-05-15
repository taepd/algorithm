
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

print(dfs(graph, 'A')) # {'A', 'F', 'D', 'E', 'B', 'C'}

# 재귀를 이용한 dfs
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print(dfs(graph, 'C')) # {'A', 'F', 'D', 'E', 'B', 'C'}

# 두 노드 간 경로 탐색
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # (node, path)
    while stack:
        (node, path) = stack.pop()
        for next in graph[node] - set(path):
            if next == goal:
                yield path + [next]  # 제너레이터로 불필요한 연산 최소화
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F')))

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

print(list(dfs_paths(graph, 'C', 'F'))) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}

# bfs 경로는 최단경로를 가장 먼저 찾는 것을 보장
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next in graph[node] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

# 제너레이터 next를 이용 최단 경로만 도출하게 할 수 있음
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']