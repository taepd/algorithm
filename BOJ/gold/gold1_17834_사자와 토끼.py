from collections import defaultdict
node, edge = map(int, input().split())

graph = defaultdict(set)

for _ in range(edge):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)


def dfs(graph, start):
    visited, block_list, stack = set(), [start], [start]
    while stack:
        node = stack.pop()
        block_flag = False if node in block_list else True
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
            if block_flag:
                block_list.extend(graph[node] - visited)
    print(set(block_list))
    return set(block_list)


ans = 0
for i in range(1, node+1):
    ans += len(dfs(graph, i))

print(ans)
