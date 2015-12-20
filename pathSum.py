# --- Introduction ---
"""
	- Given a binary tree and a sum, determine if the tree has a root-to-leaf such that
	adding up all the values along the path equals the given sum.
	- E.G:
	input:
	[5, 4, 8, 11, #, 13, 4, 7, 2, #, 1]
	sum = 22
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
		# two terminate condition: if reach the leaf and not found ,return false;
		# reach the leaf and then found, return true.
		if not root:
			return False
		elif not root.left and not root.right and sum == root.val:
			return True
		else:
			return self.hasPathSum(root.left, sum-root.val) 
			or self.hasPathSum(root.right, sum-root.val)
			