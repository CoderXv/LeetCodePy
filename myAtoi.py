# --- Introduction ---
"""
	- Implement atoi to convert a string to an integer.
	
	- Hint: Carefully consider all possible input cases. If you want a challenge, 
	please do not see below and ask yourself what are the possible input cases.
	
	- Notes: It is intended for this problem to be specified vaguely (ie, no given 
	input specs). You are responsible to gather all the input requirements up front.
	
	- Requirements for atoi:
	
	- The function first discards as many whitespace characters as necessary until the 
	first non-whitespace character is found. Then, starting from this character, takes 
	an optional initial plus or minus sign followed by as many numerical digits as 
	possible, and interprets them as a numerical value.

	- The string can contain additional characters after those that form the integral 
	number, which are ignored and have no effect on the behavior of this function.

	- If the first sequence of non-whitespace characters in str is not a valid 
	integral number, or if no such sequence exists because either str is empty or it 
	contains only whitespace characters, no conversion is performed.

	- If no valid conversion could be performed, a zero value is returned. If the 
	correct value is out of the range of representable values, INT_MAX (2147483647) or 
	INT_MIN (-2147483648) is returned.	
"""


# --- Code ---
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #only can change 0~9 int, dot operator not included.
        """
            string.strip(s, [, chars])
            - return a copy of the strings with leading and trailing character 
            removed.If chars is omitted or None, whitespace characters are removed.
            If given and not None, chars must be a string; the characters in the
            string will be stripped from the both ends of the string this method is 
            called on.
            - Changed in version 2.2.3: The chars parametres was added. The chars 
            parameter cannot be passed in earlier 2.2 versions.
        """
		if not str:
			return 0
		# delete the ahead blank 
		st = list(str.strip())
		# determine the sign
		flag = -1 if st[0] == '-' else 1
		# del the sign
		if st[0] in ['-', '+']: del st[0]
		res, index = 0, 0 
		while index < len(st) and st[index].isdigit():
			res = res*10 + ord(st[index]) - ord('0')
		res *= flag
		return max(-2**31, min(res, 2**31-1))