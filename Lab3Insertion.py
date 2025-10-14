from collections import deque
# deque stands for "double-ended queue"

# adjacency list
v = [[] for _ in range(10)]  

# level array
level = [-1] * 10  

# visited array
vis = [False] * 10  

def bfs(s):
    q = deque()
    q.append(s)
    level[s] = 0   
    vis[s] = True

    while q:
        p = q.popleft()
        for child in v[p]:
            if not vis[child]:
                level[child] = level[p] + 1
                q.append(child)
                vis[child] = True

# Example graph (undirected)
v[0].append(1)
v[1].append(0)
v[1].append(2)
v[2].append(1)
v[2].append(3)
v[3].append(2)

# Run BFS from node 0
bfs(0)

# Print node levels
for i in range(4):
    print("Node", i, "Level:", level[i])