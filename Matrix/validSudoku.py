# 36) Valid Sudoku 
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

check grid by grid (5 3 . )
                   (6 . . )
                   (. 9 8 )
        
check row 

check column 

        """
        for i in range(9):
            temp = ''.join(board[i])
            temp = temp.replace('.', '')
            if len(temp) != len(set(temp)):
                return False
        
        for j in range(9):
            temp = ''.join(board[k][j] for k in range(9))
            temp = temp.replace('.', '')
            if len(temp) != len(set(temp)):
                return False
        
        for i in range(3):
            for j in range(3):
                temp = ''.join(board[i*3+k][j*3+l] for k in range(3) for l in range(3))
                temp = temp.replace('.', '')
                if len(temp) != len(set(temp)):
                    return False
        
        
        # if it is valid: 
        return True
    