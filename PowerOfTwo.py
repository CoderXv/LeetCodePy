# --- Introduction ---
"""
	Given an integer, write a function to detemine if it's a power of two.
	The definition of 'power of two': a figure match 2^n 
	& operator in py: bitwise AND
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
		return (n > 0) and (n & (n - 1)) == 0

