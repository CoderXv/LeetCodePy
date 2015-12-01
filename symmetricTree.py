# --- Introduction ---
"""
	- Given a binary tree, check whether it is a mirror of itself(ie, symmetirc around
	its center).
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
		if not root:
			return True
		else:
			return self.isMirror(root.left, root.right)
	
	def is Mirror(self, left, right):
		if not left and right:
			return False
		if not left and not right:
			return True
		if left and not right:
			return False
		if left.val == right.val:
			outpair = self.isMirror(left.left, left.right)
			inpair = self.isMirror(right.left, right.right)
			return outpair and inpair
		else:
			return False
