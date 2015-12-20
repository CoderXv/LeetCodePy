# --- Introduction ---
# You need to completely understand the process of this program.
"""
	- Determine if a Sudoku is valid, according to: 
	- https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
	- The Sudoku board could be partially filled, where empty cells are filled with the
	character '.'.	
"""

# --- Code ---
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:return False
        m,n=len(board),len(board[0])
        check_row=[[0 for i in range(9)] for j in range(9)]
		#three 2d array to check each row, col and sub box
        check_col=[[0 for i in range(9)] for j in range(9)]
		#three 2d array to check each row, col and sub box
        check_box=[[0 for i in range(9)] for j in range(9)]
		#three 2d array to check each row, col and sub box
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] != '.':
                    num=int(board[i][j])-1 
					# need -1 becasue the index of array is 0~8
                    k=i/3*3+j/3
                    #because if previously the same number of same row,col or box have exist, it is false
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False
                    #assign value to all the checking 2d arrayes
                    check_row[i][num]=check_col[j][num]= check_box[k][num]=1
        return True