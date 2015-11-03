# --- Introduction ---
"""
	- A happy number is a number defined by the following process: Starting with any positive integer, replace the number of the square of its digits, and repeat the process until the number equal 1 (where it will stay), or it loops endlessly which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
	- E.G: 19 is a happy number:
		1^2 + 9^2 = 82
		8^2 + 2^2 = 68
		6^2 + 8^2 = 100
		1^2 + 0^2 + 0^2 = 1
"""

# --- Solution in Brief --- 
"""
	- Numbers that are happy, follow a sequence that ends in 1. All non-happy numbers follow sequence that reach the cycle:
		4, 16, 37, 58, 89, 145, 42, 20, 4, ..
	- Numbers in the above sequence were coined the term, 'despairing numbers', since happiness always ends with them.
	- So every unhappy number in the processing will meet the despairing number, which is the judgement that we can end the processing and declare the number is unhappy.
	- map(para1, para2) function is a BIF in Py, which is used for parse all of the elements in the para2 with the method of para1, returning elements which has been processed.
	- pow(x, y) function is also a BIF, which means x ^ y, then returning the result.
	- sum(para) function is also a BIF, which returns the sum of elements in para.
	- x // y returns (floored) quotient of x and y.
"""
# --- Program ---
class Solution(object):
	def isHappy(self, number):
	"""
	:type number: int
	:rtype: bool
	"""
	if number == 1:
		return True
	elif number == 4:
		return False
	else:
		return self.isHappy(self.happy(number))
		
	def square(self, number):
		return int(number) * int(number)
		
	def happy(self, number):
		return sum(map(self.square, list(str(number))))