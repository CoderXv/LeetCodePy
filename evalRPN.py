# --- Introduction ---
"""
	- Evaluate the value of an arithmatic expression in Reverse Polish Notation.
	- Valid operators are + - * /. each operad may be an integer or another expression.
	- E.G:
		["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
		["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

# --- Code ---
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
	
		num_stk = []
		for token in tokens:
			# isdigit() is only suitable for non-negative figure.
			if token not in ["+", "-", "*", "/"]:
				num_stk.append(int(token))
			else:
				op1, op2,  = num_stk.pop(), num_stk.pop()
				if token == '+':
					temp = op1 + op2
					num_stk.append(temp)
				elif token == '-':
					temp = op1 - op2
					num_stk.append(temp)
				elif token == '*':
					temp = op1 * op2
					num_stk.append(temp)
				else:
					# here take care of the case like '1/-22',
					# in Py 2.x it returns -1, while in
					# Leetcode it should return 0.
					if op1 * op2 <0 and op1%op2 != 0:
						num_stk.append(op1/op2+1)
					else:
						num_stk.append(op1/op2)
				# print num_stk
			return num_stk.pop()
		