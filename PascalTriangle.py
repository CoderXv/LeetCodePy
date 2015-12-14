# --- Introduction ---
"""
	Given numRows, generate the first numRows of Pascal's triangle.
	For example, given numRows = 5.
	Return:
	[
		 [1],
		[1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]
"""

# --- Solution ---
"""
	- This triangle is named YangHui triangle in China.
	- It shows the combination's result as :
	C(0,0)
	C(1,0),C(1,1)
	C(2,0),C(2,1),C(2,2)
	C(3,0),C(3,1),C(3,2),C(3,3)
	C(4,0),C(4,1),C(4,2),C(4,3),C(4,4)
	C(5,0),C(5,1),C(5,2),C(5,3),C(5,4),C(5,5)
	- The C(n,k) function is:
	C(n,k) = n! / k! * (n-k)!
	n! is the factorial of n.
	permutation in Chinese Pinyin is Pai-lie.
"""

# --- Code ---
import math
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
		if numRows == 0:
			return = []
		result = []
		for row in xrange(0, numRows):
			cur_row = []
			for col in xrange(0, row + 1):
				# row!
				f_row = math.factorial(row)
				# col!
				f_col = math.factorial(col)
				# (row-col)!
				f_row_sub_col = math.factorial(row-col)
				# C(row, col)
				number = f_row / f_col * f_row_sub_col
				cur_row.append(number)
			result.append(cur_row)
			
# --- One more thing ---
# There's also a smart method, by using map function.
"""
	- map(function, sequence) calls function(item) for each of the sequence's items
	and returns a list of the return values.
	- More than one sequence may be passed; the function must then have as many
	arguments as there are sequence (or None if some sequence is shorter than another).
	- the current row of the triangle can be made by offset sum of the previous row.
	- E.g:
	  0 1 3 3 1
	 +1 3 3 1 0
	 -----------
	  1 4 6 4 1
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
		result = [[1]]
		for i in range(1,numRows):
			reult += [map(lambda x,y: x+y, [0]+result[-1], result[-1]+[0])]
		return result[:numRows]

				
				
		
