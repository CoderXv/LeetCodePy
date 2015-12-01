# --- Introduction ---
"""
	- Implement a basic calculator to evaluate a simple expression str.
	- The expression str may contain open( and closing parentheses), the plus + or minus
	sign -, non-negative integers and empty spaces.
	- You may assume that the given expression is always valid.
"""

# --- Code ---
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
		# isdigit() is also available in python.
		seq = []
		# ops = []
		num = 0
		result = 0
		flag = 1
		for c in s:
			if c.isdigit():
				num = num*10 + int(c)
				continue
			# if it's not a digit, just sum the previous number.
			# you need to confirm the order.
			result += flag*num
			num = 0
			
			if c == '-':
				flag = -1 
			elif c == '+':
				flag = 1 
			elif c == '(':
				seq.append(result)
				seq.append(flag)
				flag = 1 
				result = 0
			elif c == ')':
				result *= seq.pop() # flag is in upper pos.
				result += seq.pop() # result from inner parentheses
		result = result + flag * num
		# add the last number of the string
		return result
		return result