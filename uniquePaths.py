# --- Introduction ---
"""
	- A robot is located at the top-left corner of a m * n gird(marked 'Start' in the 
	diagram below)
	- The robot can only move either down or right at any point in time. The robot is 
	trying to reach the bottom-right corner of the gird(marked 'Finish' in the diagram
	below)
	- How many possible unique paths are there?
"""

# --- Solution and Code ---
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
		# make a matrix m * n
		matrix = [[1]*n]*m
		# Dynamic Programming: When we reach the i*j point, Current path number is based
		# on two previous results of the position: matrix[i][j-1] and matrix[i-1][j]
		# So we parse the matrix and the result is the matrix[m-1][n-1]
		
		for i in xrange(1, m):
			for j in xrange(1, n):
				matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
		return matrix[m-1][n-1]

		
# Optimise:
"""
	- You may have obeserved that each tiem when we update matrix[i][j]. We only need 
	matrix[i-1][j] (at the same column) and the path[i][j-1](at the left column). So it
	is enough to maintain two columns(the current column and the left column) instead 
	of maintaining the full m*n matrix. Now the code can be optimised to have 
	O(min(m,n)) space comlexity
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
		if m > n:
			return self.uniquePaths(n, m)
		pre = [1] * m
		cur = [1] * n
		for j in range(1, n):
			for i in range(1, m):
				cur[i] = cur[i-1] + pre[i] 
			pre, cur = cur, pre
		return pre[m-1]

		
# Optimise Ver.2:
"""
	- Further inspecting the above code, we find that keeping two columns is used to 
	recover pre[i], which is just cur[i] before its update. So there is even no need 
	to use two vectors and one is just enough. Now the space is further saved and the 
	code gets more shorter
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
		if m > n:
			return self.uniquePaths(n, m)
		cur = [1] * m
		for j in range(1, n):
			for i in range(1, m):
				cur[i] += cur[i-1]
		return cur[m-1]
		
		
		
		
		
		
		
		
		
		
		
		
		