from collections import deque

def bfs(graph, start):
    visited = set()           # to keep track of visited nodes
    queue = deque([start])    # queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
print("BFS traversal starting from A:")
bfs(graph, 'A')