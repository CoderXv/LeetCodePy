# --- Introduction ---
"""
	- Given a binary Tree, return all root-to-leaf paths.
	- E.G:
		Input:
			[1, 2, 3, 5]
		Return:
			["1->2->5", "1->3"]
	Tag: Tree, Depth-first-search
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
		if not root:
			return []
		string = ""
		list = []
		self.findPath(root, string, list)
		return list
	
	def findPath(root, string, list):
		if not root.right and root.left:
			string = string + str(root.val)
			list.append(string)
			return 
		newstr = string + str(root.val) + "->"		
		if root.left:
			self.findPath(root.left, newstr, list)
		if root.right:
			self.findPath(root.right, newstr, list)