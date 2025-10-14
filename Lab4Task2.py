def find_words(board, dictionary):
    rows, cols = len(board), len(board[0])
    words = set()
    visited = [[False] * cols for _ in range(rows)]

    # Eight directions: North, East, South, West, NE, NW, SE, SW
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

    def dfs(row, col, current_word):
        current_word += board[row][col]
        if current_word in dictionary:
            words.add(current_word)
        
        visited[row][col] = True
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not visited[new_row][new_col]):
                dfs(new_row, new_col, current_word)
        visited[row][col] = False  # Backtrack

    # Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, "")

    return list(words)

# Boggle board from the image
board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

# Dictionary of valid words
dictionary = {'NOTE', 'SAND', 'STONED', 'START'}

# Find and print all possible words
result = find_words(board, dictionary)
print("Possible words:", result)