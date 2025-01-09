from typing import List
import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        board_copy = copy.deepcopy(board)
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_neighbors = self.count_live_neighbors(board_copy, i, j)
                if board_copy[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                else:
                    if live_neighbors == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0

    def count_live_neighbors(self, board: List[List[int]], i, j) -> None:
        live_neighbors = 0
        rows, cols = len(board), len(board[0])
        for x in range(max(0, i-1), min(rows, i+2)):
            for y in range(max(0, j-1), min(cols, j+2)):
                if x != i or y != j:
                    live_neighbors += board[x][y]
        return live_neighbors

sol = Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))