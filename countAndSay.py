# --- Introduction ---
"""
	- The count-and-say sequence is the sequence of integers beginning as follows:
	- 1, 11, 21, 1211, 111221, ...
	- 1 is read off as "one 1" or 11
	- 11 is read off as "two 1s" or 21
	- 21 is read off as "one 2, then one 1" or 1211
	- Given an integer n, generate the n-th sequence.
	- Note: The sequence of integers will be represented as a string
"""

# --- Discribe ---
"""
	1
	11 
	21 
	1211 
	111221 
	312211
	13112221
	...
"""

# --- Code ---
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype
		"""
		# save for the previous result.
		s = ["1"]
		result = "1"
		# the n-th sequence, input 1 should output '1'
		for i in xrange(n-1):
			start = 0
			temp = []
			# process one sequence, scan from start to end.
			while start < len(s):
				count = 1
				next = start + 1 
				# Scan until s[next] is different.
				while next < len(s) and s[start] == s[next]:
					count += 1
					next += 1 
				# Get the new item in.
				temp.append(str(count))
				temp.append(s[start])
				# Start from the next one 
				start = next 
			# Concatenate list into string.
			result = ''.join(temp)
			s = temp 
		return result
