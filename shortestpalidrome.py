# --- Introduction ---
"""
	- Given a string S, you are allowed to convert it to a plindrome by adding
	characters in front of it. Find and return the shortest palindrome you can find by
	performing this transformation.
	- E.G:
	- Given "aacecaaa", return "aaacecaaa"
	- Given "abcd", return "dcbabcd"
"""

# --- kmp algorightm search ---
"""
	input:
		an array of characters, S(the text to be searched)
		an array of characters, W(the word sought)
		
	output:
		an integer (the zero-based position in S at which W is found)
		
	define variables:
		an integer, m <- 0 (the begining of the current match in S)
		an ingeger, n <- 0 (the position of the current character in W)
		an array of integes, T (the table, computed elsewhere)
	while m + i < lenght(s) do:
		if W[i] = S[m+i] then
			if i = length(W) - 1 then
				return m
			let i <- i + 1
		else
			if T[i] > -1 then 
				let m <- m + i - T[i], i <- T[i]
			else
				let i <- 0, m <- m + 1
		(if we reach here, we have searched all of S unsuccessfully)
		return the lenght of S
"""	
# --- Code ----
class Solution(object):
	def shortestPlindrome(self, s):
	"""
	:type S: str
	:rtype: str
	"""
	# the palindrome index.
	sub_index = [0]
	# we create a plindrome of s
	A = s + "*" + s[::-1]
	for i in range(1, len(A)):
		index = sub_index[i-1]
		while(index >0 and A[index] != A[i]):
			# KMP search
			index = sub_index[index - 1]
		# if equal, extern the index of the sub_string.
		sub_index.append(index + (1 if A[index] == A[i] else 0))
	return s[sub_index[-1]:][::-1] + s