# --- Introduction ---
# 94. Binary Tree Inorder Traversal
"""
	- Given a binary tree, return the inorder traversal of its node's values.
"""


# --- Code ---

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# --- Recursively --- 
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode 
		:rtype: List[int]
		"""
		stk = []
		res = []
		self.inorder(root, stk, res)
	
	def inorder(self, root, stk, res):
		if root:
			stk.append(root)
			root = root.left 
			self.inorder(root, stk, res)
		if not stk:			
			return res
		root = stk.pop()
		res.append(root.val)
		root = root.right 
		self.inorder(root, stk, res)


# --- Iteratively ---
class Solution(object):
	class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode 
		:rtype: List[int]
		"""
		stk = []
		res = []
		while True:
			while root:
				stk.append(root)
				root = root.left 
			if not stk:
				return res 
			root = stk.pop()
			res.append(root.val)
			root = root.right 
		
		return res 











		
	
	