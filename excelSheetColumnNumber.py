# --- Introduction ---
"""
	- Given a column title as appear in an Excel sheet, return its corresponding 
	column number.
	- For example:
		A -> 1
		B -> 2
		C -> 3
		...
		Z -> 26
		AA -> 27
		AB -> 28
"""

# --- Code ---
# base 26 to base 10
# Captial in default.
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
		return reduce(lambda x, y: x*26 + y, [ord(c) - 64 for c in list(s)])
		

# --- Introduction ---
"""
	- Given a positive integer, return its corresponding column title as appear in an 
	Excel sheet.
	- For example:
		1 -> A
		2 -> B
		3 -> C
		...
		26 -> Z
		27 -> AA
		28 -> AB 
"""

# base 10 to base 26
# Captial in default.
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
		if n == 0:
			return ""
		else:
			return self.convertToTitle((n - 1) / 26) 
			+ chr((n - 1) % 26 + ord('A'))