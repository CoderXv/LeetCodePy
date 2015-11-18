# --- Introduction ---
"""
	- Given two binary trees, write a function to check if they are equal or not.
	- Two binary trees are considered equal if they are structurally identical and the
	nodes have the same values.
"""

# --- Code ---
# sloved recursively.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
	def isSameTree(self, q, p):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if q and p:
			return q.val == p.val and self.isSameTree(q.left, p.left) and
			self.isSameTree(q.right, p.right)
		else:
			q == p