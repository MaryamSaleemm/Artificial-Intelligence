def is_safe(assignment, row, col):
    """
    assignment: dict mapping placed rows -> column (0..3)
    row: row we want to place now
    col: candidate column
    """
    for r, c in assignment.items():
        # same column
        if c == col:
            return False
        # same diagonal
        if abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n=4):
    solutions = []

    def backtrack(row, assignment):
        if row == n:
            # found complete assignment; store as list of columns
            solutions.append([assignment[r] for r in range(n)])
            return

        for col in range(n):
            if is_safe(assignment, row, col):
                assignment[row] = col
                backtrack(row + 1, assignment)
                del assignment[row]  # backtrack

    backtrack(0, {})
    return solutions

def print_board(solution):
    n = len(solution)
    for r in range(n):
        row = ['.'] * n
        row[solution[r]] = 'Q'
        print(' '.join(row))
    print()

if __name__ == "__main__":
    sols = solve_n_queens(4)
    print(f"Found {len(sols)} solution(s).\n")
    for i, sol in enumerate(sols, 1):
        print(f"Solution {i}: columns = {sol}")
        print_board(sol)