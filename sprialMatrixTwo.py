# --- No.59 Spiral Matrix II ---
"""
	- Given an integer n, generate a square matrix filled with elements from 1 to n**2 
	in spiral order.
	- For example, 
	- Given n = 3, 
	- You should return the following matrix:
	[[1,2,3],[8,9,4],[7,6,5]]
"""

# --- Solutions ---
"""
	For anti-clockwise direction:
	1. from left to right 
	2. from up to bottom
	3. from left to right 
	4. from bottom to right 
"""
# --- Code ---
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
		matrix = [[0 for i in xrange(n)] for i in xrange(n)]
		k = 1
		i = 0
		while k <= n*n:
			# horizontal, from left to right 
			j = i 			
			while j < n - i:
				matrix[i][j] = k
				k += 1
				j += 1
			# vertical, from up to bottom 
			j = i + 1
			while j < n - i:
				matrix[j][n - i - 1] = k
				k += 1
				j += 1
			# horizontal, from right to left
			j = n - i - 2  # attention please!
			while j > i:
				matrix[n - i - 1][j] = k 
				k += 1
				j -= 1
			# vertical, from bottom to up 
			while j > i:  # attention please!
				matrix[j][n - i - 1] = k 
				k += 1
				j -= 1		
			
			# each step end, the row or col will add 1.
			i += 1
			return matrix 