# --- Introduction ---
"""
	- Given a non-negative integer num, repeatedly add 
	all its digits until the result has only one digit.
	- E.G:
	- Given num = 38, the process is like: 3 + 8 = 11, 
	1 + 1 = 2. Since 2 has only one digit, return it.
	* Follow up:
		Could you do it without any loop/recursion in O(1) runtime?
	- Hint:
		A naive implementation of the above process is trivial. 
		Could you come up with other methods?
		What are all the possible results?
		How do they occur, periodically or randomly?
		See this module as Digital Roots.
"""
# --- Solution in Brief ---
"""
	- This question is a classical math module called Digital Root.
	- It helps to see the digital root of a positive integer as the
	position as the position it holds with respect to the largest 
	multiple of 9 less than it. For example, the digital root 
	of 11 is 2, which means that 11 is the second number after 9. 
	Likewise, the digital root of 2035 is 1, which means that 2035 -1 
	is a multiple of 9. if a number produces a digital root of 
	exactly 9 then the number is a multiple of 9.
	- With this in mind the digital root of 
	a positive integer n may be defined by using floor function Rounding Up (x), 
	as

		- dr(n) = n - 9* Rounding UP((n-1)/9)	
"""
# --- Program ---
class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if num == 0:
			return 0
		elif num > 0:
			return (num - 9 * ((num - 1 / 9)))