# 289) Game of Life
from collections import List 

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])

        # 8 directions cell can interact with
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1) ]

        def countLiveCells(row, col):
            count = 0
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and (board[new_row][new_col] == 1 or board[new_row][new_col] == -1):
                    count += 1
            
            return count

        for i in range(m):
            for j in range(n):
                live_cells = countLiveCells(i, j)

                if board[i][j] == 1 and (live_cells < 2 or live_cells > 3):
                    # mark live cells that will become dead in next state as -1
                    board[i][j] = -1
                
                elif board[i][j] == 0 and live_cells == 3:
                    # mark dead cells that will become live in next state as 2
                    board[i][j] = 2

        # update board based on marked cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

