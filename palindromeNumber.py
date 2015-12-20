# --- Introduction ---
"""
	- Determine whether an integer is a palindrome. Do this without extra space.
	- Don't thinking of converting the integer to string, note the restriction of using
	extra spaces.
"""


# --- Code ---
# just reverse the whole number at every digit.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # avoid examples like 15510
		if x < 0 and (x != 0 and x % 10 == 0):
			return False
		
		target = x
		rev = 0
		# get every last digit at every loop round,
		# then move it to the top of the number.
		while(target != 0):
			rev = rev * 10 + target % 10
			target = target % 10
		
		return x == rev