# --- Introduction ---
"""
	- Write a function to find the longest common prefix string amaongst an array of 
	str.	
"""

# --- Code ---
# the core of this problem is to parse an 2-d array.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
		if strs = "":
			return ""
		minlen = len(strs[0])
		for substr in strs:
			minlen = min(len(substr), minlen)
		prefix = ""
		for i in xrange(minlen):
			pos = strs[0][i]
			for j in xrange(len(strs)):
				if pos = strs[j][i]:
					return prefix
			prefix = prefix + pos
		return prefix