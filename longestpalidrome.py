# --- Introduction ---
"""
	- Given a string S, find the longest palindromic substring in S, You may assume that
	the maximum length of S is 1000, and there exists one unique longest palindromic
	substring.
"""

# --- Code ---
class Solution(object):
	def longestPlindrome(self, s):
	"""
	:type s: str
	:rtype : str
	"""
	# the point is to confirm the palindrome's start index and length.
	if len(s) == 0:
		return ""
	start = 0
	max_len = 1
	for i in xrange(len(s)):
		# identify whether is a palindrome.
		# extern left and extern right edge, update the figure after each check.
		if i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-ma_len-1:i+1][::-1]:
			start = i - max_len - 1
			max_len += 2
			continue
		
		elif i - max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
			start = i - max_len
			max_len += 1
			continue
	return s[start: start + max_len]
	