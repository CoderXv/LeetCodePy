# --- Introduction ---
"""
	- Given n , generate all structurally unique BST's (binary search trees) that store
	value 1...n
	- E.G:
	- Given n = 3, your program should return all 5 unique BST's shown.
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def generateTrees(self, n):
	"""
	:type n: int
	:r type: ListNode[TreeNode]
	"""
		if n == 0:
			return []
		return self.build(1, n+1)
	def build(self, start, end):
		if start == end:
			return None
		result = []
		for i in xrange(start, end):
			for left in self.build(start, i) or [None]:
				for right in self.build(i+1, end) or [None]:\
					node = TreeNode(i)
					node.left, node.right = left, right
					result.append(node)
		return result
		