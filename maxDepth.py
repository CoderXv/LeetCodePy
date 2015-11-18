# --- Introduction ---
"""
	- Given a binary tree, find its maximum depth.
	- The maximum depth is the number of nodes along the longest path from the node down
	to the farthest leaf node.
"""

# --- Code ---
# DFS search
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0
		depth = 0		
		stk = [root]
		while stk:
			next_level = []
			depth += 1
			for item in stk:
				if item.left:
					next_level.append(item.left)
				elif item.right:
					next_level.append(item.right)
			stk = next_level
		return depth
