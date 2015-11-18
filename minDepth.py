# ---Introduction---
"""
	- Given a binary tree, find its minimum depth.
	- The minimum depth is the number of nodes along the shortest path from the root
	node down to the nearst leaf node.
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS solution.
class Solution(object):
	def minDepth(self, root):		
		next_level = []
		if root == None:
			return 0
		if root.right == None or root.right ==None:
			return (self.minDepth(root.left) + self.minDepth(root.right) + 1)
		return (min(self.minDepth(root.left), self.minDepth(root.right)) + 1)
		
# BFS solution
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
        """