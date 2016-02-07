# --- Introduction ---
"""
	- Given a string array words, find the maxium value of length(word[i]) * 
	length(word[j]) where the two words do not share common letters. You may assume that
	each word will contain only lower case letters. If no such word exist, return 0.
	
	- Example 1:
		Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
		Return 16
		The two words can be "abcw", "xtfn".
	- Example 2:
		Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
		Return 4
		The two words can be "ab", "cd".
		
	- Example 3:
		Given ["a", "aa", "aaa", "aaaa"]
		Return 0
		No such pair of words.
		
"""

# --- Solution ---
"""
	- 这里我们使用暴力搜索法，首先我们遍历一遍输入的字符串数组，然后使用一个辅助数组来
	存储每个字字符串的字母的情况。
		1 << (ord(c) - ord('a'))
		对于这行代码，如果 1 << 2, 结果为4， 等价于2*2，所以这行代码的意义就是存储每个
		单词中的字母的情况，每一位对应的字母情况都进行了存储。
	- 然后针对现在的辅助字符串进行时间复杂度为n^2的遍历，找出彻底没有交集的子字符串，
	求出长度乘积之后与最大值进行比对。
	- 总体来说时间复杂度为n^2，空间复杂度为n
"""

# --- Code ---
class Solution(Object):
	def maxProduct(self, words):
	"""
	:type words: List[str]
	:rtype: int 
	"""
	if not words:
		return 0
	
	mask = [0] * len(words)
	ans = 0
	
	for i, w in enumerate(words):
		for c in w:
			mask[i] |= 1 << (ord(c) - ord('a'))
		
		for j in xrange(i):
			if not mask[i] & mask[j]:
				ans = max(ans, len(words[i]) * len(words[j]))
				
	return ans
	
	
	
	
	
	
	
	
	
	
	