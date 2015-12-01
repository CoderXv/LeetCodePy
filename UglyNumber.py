# --- Introduction ---
"""
	- Write a program to check whether a ugly number.
	- Ugly numbers are positive numbers whose prime factor only include 2, 3, 5. 
	- E.G:
		6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
	- Note that 1 is typically treated as an ugly number.
"""

# --- Solution in Brief ---
"""
	- devided 2, 3, 5 in loop one after another to
	see the ultimate residence is 1 or not.
"""

# --- Program ---
class Solution(object):
	def isUgly(self, num):
	"""
	:type num: int
	:rtype: bool
	"""
	if num == 1:
		return True
	elif num == 0:
		return False
	else:
		while num % 2 == 0:
			num /= 2
		if num == 1:
			return True
		while num % 3 == 0:
			num /= 3
		if num == 1:
			return True
		while num % 5 == 0:
			num /= 5
		if num == 1:
			return True
		else:
			return False