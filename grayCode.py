# --- Introduction ---
"""
	- The Gray Code is a binary numeral system where two successive values differ in
	only one bit.
	- Given a non-negative integer n representing the total number of bits in the code,
	print the sequence of gray code. A gray code sequence must begin with 0.
	- For example, given n=2, return[0,1,3,2].Its gray code sequence is:
	00 - 0
	01 - 1
	11 - 3
	10 - 2
	- Note:
	- For a given n, gray code sequence is not uniquely defined.
	- For example, [0,2,3,1] is also a valid code sequence according to the above
	definition.
"""

# --- Code ---
class Solution(object):
	def grayCode(self, n):
	"""
	: type n: int 
	: rtype: List[int]
	"""
	# Industrial Gray Code Creating
	# Each bit is inverted if the next higher bit of the input value is set to one.
	return [(i>>1)^i for i in range(2**n)]
