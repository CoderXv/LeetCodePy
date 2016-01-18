# --- Introduction ---
"""
	- Reverse digits of an interger.
	- example1: x = 123 return 321
	- example2: x = -123 return -321
"""

# --- Attention ---
"""
	- Tricks in this Question!
	- If the intger's last digits is 0, what should the output be? ie, case such as 100
	- Did you notice that the reversed intger might overflow? Assume the input is a 32
	bit integer, then the reverse of 1000000003 overflows. How should you handle such
	cases?
	- For the purpose of this problem, assume that your funcion returns 0 when the
	reversed integer overflows.
"""

# --- Code ---
# Firstly, input such as 100, 1000, we return 1.
# Secondly, python doesn't have overflow condition, for it's an automatic data type.
# sys.maxint equals to 2147483647
import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
		if x < -sys.maxint or x > sys.maxint:
			return 0
			
		strx = str(x)
		# negative condition.
		if strx[0] == '-':
			strx_rev = '-' + strx[1:][::-1]
			if int(strx_rev) < -2147483647:
				return 0
			else:
				return int(strx_rev)
		
		strx_rev = strx[::-1]
		if int(strx_rev) > 2147483647:
			return 0
		else:
			return int(strx_rev)
		
		
		
		
		
		
		
		
		
