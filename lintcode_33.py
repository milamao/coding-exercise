class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        results = []
        used_cols = []
        self.search(n, used_cols, results)
        return results

    def search(self, n, used_cols, results):
        row = len(used_cols)  # current row
        if row == n:
            self.draw_board(used_cols, n, results)
            return
        for col in range(n):
            if not self.can_place(row, col, used_cols, n):
                continue
            used_cols.append(col)
            self.search(n, used_cols, results)
            used_cols.pop()

    def can_place(self, row, col, used_cols, n):
        for r, c in enumerate(used_cols):
            if c == col:  # same column
                return False
            if r + c == row + col or r - c == row - col:  # same diagonal
                return False
        return True

    def draw_board(self, used_cols, n, results):
        board = []
        for col in used_cols:  # every row
            board.append(''.join(['Q' if j == col else '.' for j in range(n)]))  # every column
        results.append(board)