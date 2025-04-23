def solve_n_queens(n):
    board = [["_" for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == "Q":
                return False
        return True

    def backtrack(row):
        if row == n:
            solution = ["".join(r) for r in board]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "_"

    backtrack(0)
    return solutions


n = 4
for solution in solve_n_queens(n):
    for row in solution:
        print(row)
    print()
