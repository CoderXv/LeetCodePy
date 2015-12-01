# --- Introduction ---
"""
	- Given n, how many structurally unique BST's that store valus 1..n?
"""

# --- Code ---
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Unique[i] = Sum(Unique[0:k]*Unique[i-1-k]), (0<=k<=i-1)
        """
		if n == 0 or n == 1:
			return 1
		unique = []
		unique.append(1) # 0 node
		unique.append(1) # 1 node
		for i in range(2, n+1):
			temp = 0
			for k in range(0, i):
				temp += unique[k]*unique[i-1-k]
			unique.append(temp)
		return unique[n]