# --- Introduction ---
"""
	- Given a string, determine if it is a palindrome, considering only alphanumeric
	and ignoring cases.
	- I.E:
	- "A man, a plan, a canal: Panama" is a palindrome.
	- "race a car" is not a palindrome.
"""

# --- Code ---
# only consider alphanumeric characters and ignoring cases.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
		# Here we introduce two BIF in Python: lower() and isalnum()
		# isalnum
		# Return true if all characters in the string are alphanumeric and there is at 
		# least one character, false otherwise
		# lower
		# Return a copy of the string with all the cased characters [4] converted to 
		# lowercase.
		# Cased characters are those with general category property being one of ¡°Lu¡± 
		# (Letter, uppercase), ¡°Ll¡± (Letter, lowercase), or ¡°Lt¡± (Letter, titlecase)
		# find all alphanumeric character and create a new list with them
		# then compare it with reverse one of itself.
		NewS = [i.lower() for i in s if i.isalnum()]
		return NewS == NewS[::-1]
		