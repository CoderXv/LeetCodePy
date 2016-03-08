# --- Introduction ---
# 22. Generate Parentheses
"""
	- Given n pairs of parentheses, write a function to generate all combinations of 
	well-formed parentheses.
	- For example, given n = 3, a solution set is:
	"((()))", "(()())", "(())()", "()(())", "()()()"
"""


# --- Solution ---
"""
	- The idea is intuitive. Use two integers to count the remaining left parentheses(n)
	and the right parentheses(m) to be added.
	- At each function call add a left parentheses if n > 0 and add a right parentheses
	if m > 0.
	- Append the result and terminate recursive calls when both m and n are zero.
"""

# --- Code ---
class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int 
		:rtype: List[int]
		"""
		res = []
		return self.helper(res, "", n, m)
		  
	
	def helper(self, res, str, n, m):
		if n == 0 and m == 0:
			res.append(str)
			return res 
		
		if n > 0:
			self.helper(res, str+"(", n-1, m+1)
		
		if m > 0:
			self.helper(res, str+")", n, m-1)

			
"""
 left n=  3 m =  0
( left n=  2 m =  1
(( left n=  1 m =  2
((( right n=  0 m =  3
((() right n=  0 m =  2
((()) right n=  0 m =  1
((())) n=  0 m =  0
(( right n=  1 m =  2
(() left n=  1 m =  1
(()( right n=  0 m =  2
(()() right n=  0 m =  1
(()()) n=  0 m =  0
(() right n=  1 m =  1
(()) left n=  1 m =  0
(())( right n=  0 m =  1
(())() n=  0 m =  0
( right n=  2 m =  1
() left n=  2 m =  0
()( left n=  1 m =  1
()(( right n=  0 m =  2
()(() right n=  0 m =  1
()(()) n=  0 m =  0
()( right n=  1 m =  1
()() left n=  1 m =  0
()()( right n=  0 m =  1
()()() n=  0 m =  0
"""