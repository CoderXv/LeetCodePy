# ---Introduction---
"""
	- Given a string S, find the longest palindrome substring in S. You may assume that 
	the maximum length of S is 1000, and there exists one unique longest palindromic
	substring.
"""

# ---Brief Solution---
"""
	- The point of code is to confirm the start index of palindrome and its length.
"""

# ---Code---
class Solution(object):
	def longestPalindrome(self, s):
	"""
	:type s: str
	:rtype: str
	"""
	# the point is to confirm the parlindrome's start index and length.
	if len(s) == 0:
		return ""
	start = 0
	max_len = 1 
	for i in xrange(len(s)):
		if i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
			start = i - max_len - 1 
			max_len += 2
			continue
		
		elif i - max_len >= 0 and s[i-max_len:i+1] == s[s-max_len:i+1][::-1]
			start = i - max_len
			max_len += 1 
			continue
	
	return s[start:start+max_len]