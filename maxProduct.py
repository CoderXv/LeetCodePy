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
	- ��������ʹ�ñ������������������Ǳ���һ��������ַ������飬Ȼ��ʹ��һ������������
	�洢ÿ�����ַ�������ĸ�������
		1 << (ord(c) - ord('a'))
		�������д��룬��� 1 << 2, ���Ϊ4�� �ȼ���2*2���������д����������Ǵ洢ÿ��
		�����е���ĸ�������ÿһλ��Ӧ����ĸ����������˴洢��
	- Ȼ��������ڵĸ����ַ�������ʱ�临�Ӷ�Ϊn^2�ı������ҳ�����û�н��������ַ�����
	������ȳ˻�֮�������ֵ���бȶԡ�
	- ������˵ʱ�临�Ӷ�Ϊn^2���ռ临�Ӷ�Ϊn
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
	
	
	
	
	
	
	
	
	
	
	