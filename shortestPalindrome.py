# --- Shortest Palindrome---
"""
	- Given a string S, you are allowed to convert it to a palindrome by adding
	characters in front of it. Find and return the shortest palindrome you can find by
	performing this transformation.
	- For example:
	- Given "aacecaa", return "aaacecaaa"
	- Given "abcd", return "dcbabcd"
"""

# --- Code ---
# Use Kmp matching algorithm to optimize the shortest palindrome.
class Solution(object):
	def shortestPalindrome(self, s):
	"""
	:type s: str
	:rtype: str
	"""
	# the longest parlindrome index
	sub_index = [0]
	# init the parse list.
	A = s + "#" + s[::-1]
	for i in range(1, len(A)):
		index = sub_index[i-1]
		while(index>0 and A[index] != A[i]):
			#KMP
			index = sub_index[index-1]
		# if equal, extern the index of the sub_string.
		sub_index.append(index+(1 if A[index]==A[i] else 0))
	return s[sub_index[-1]:][::-1] + s
	
	