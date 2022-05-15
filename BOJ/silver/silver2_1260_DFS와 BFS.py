import sys
from collections import deque


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


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                tmp = list(set(graph[node]) - set(visited))
                stack.extend(sorted(tmp, reverse=True))  # 가장 작은 수부터 pop하기 위해

    return visited

input = sys.stdin.readline
n_node, n_edge, start = map(int, input().split())

graph = {}
for i in range(n_edge):
    n1, n2 = map(int, input().split())

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)


print(*dfs(graph, start))
print(*bfs(graph, start))


# # 경량화
# # 복잡하기만 하고 큰 성능향상은 없음 300 -> 288
# import sys
# from collections import deque
#
#
# def bfs(graph, root):
#     visited = []
#     queue = deque([root])
#
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             if graph[node]:
#                 tmp = list(set(graph[node]) - set(visited))
#                 queue.extend(sorted(tmp))
#
#     return visited
#
#
# def dfs(graph, root):
#     visited = []
#     stack = [root]
#
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             if graph[node]:
#                 tmp = list(set(graph[node]) - set(visited))
#                 stack.extend(sorted(tmp, reverse=True))  # 가장 작은 수부터 pop하기 위해
#
#     return visited
#
# input = sys.stdin.readline
# n_node, n_edge, start = map(int, input().split())
#
# graph = [[] for _ in range(max(n_node, n_edge) + 1)]  # 이중 list로 조건문 분기 절약/ 간선없는 시작 node 예외 처리 위해 max적용
#
# for i in range(n_edge):
#     n1, n2 = map(int, input().split())
#
#     graph[n1].append(n2)
#     graph[n2].append(n1)
#
# print(*dfs(graph, start))
# print(*bfs(graph, start))

