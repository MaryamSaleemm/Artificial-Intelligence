from collections import deque

# Maze (0 = wall, 1 = open path)
maze = [
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0]
]

# Start and Goal positions
start = (5,1)   # row=5, col=1  (yellow smiley position)
goal  = (1,5)   # row=1, col=5  (goal position)

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([[start]])  # queue holds paths
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == goal:
            return path  # shortest path found

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_path = list(path)  #make the copy of the path
                    new_path.append((nx, ny)) #append the new path 
                    queue.append(new_path)

    return None

# Run BFS
path = bfs(maze, start, goal)
print("Shortest Path:", path)