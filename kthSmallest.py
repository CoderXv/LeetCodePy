# --- Introduction ---
"""
	- Given a binary search tree, write a function kthSmallest to find the kth smallest
	element in it.
	- Note:
	You may assume k is always valid, 1 <= k <= BST's total element.
	- Follow Up:
	What if the BST is modified(insert/delete operations) often and you need to find the
	kth smallest frequently? How would you optimize the kthSmallest routine?
	- Hint: 
		1. Try to utilize the property of a BST.
		2. What if you could modify the BST node's structure?
		3. The optimal runtime complexity is O(height of BST)
"""

# --- Solution ---
"""
	1. Binary search:
		if the k is bigger than number of nodes in left tree, then we search the right
	part of it, from left part to right part, until we find the kth element.
	2. DFS search:
		Firstly we find the first smallest of the node, then consider the k's value, 
	return to the previous layer's node, then consider it's right child tree, then 
	make the k -1, do this recursively or iteratively until we find the target
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# --- Binary Search ---
class Solution(object):
	def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
		# count the left child-tree
		count  = self.countNodes(root, k)
		
		if k <= count:
			self.countNodes(root.left, k)
		elif k > count + 1:
			self.countNodes(root.right, k - 1 - count)
		
		return root.val
		
	def countNodes(self, root, k):
		if root is None:
			return 0
		else:
			return 1 + self.countNodes(root.right) + self.countNodes(root.right)
			
# --- DFS iteratively ---
class Solution(object):
	def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
		stk = []
		while root.right:
			stk.append(root)
			root = root.right 
		while k != 0:
			count -= 1
			node = stk.pop()
			if k == 0:
				return node.val 
			node = node.right
		while node:
			stk.append(node)
			node = node.left 
		
		# error occur
		return -1
	
		


# --- DFS Recursively ---
class Solution(object):
	def __init__(self, parent=None):
		self.number = 0
		self.count = 0
	
	def kthSmalleest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		self.count = k
		self.helper(root)
		return self.number 
		
	def helper(self, n):
		if n.left is not None:
			self.helper(n.left)
		self.count -= 1
		
		if self.count == 0:
			self.number = n.val
			return 
		
		if n.right is not None:
			self.helper(n.right)


			
	
	
	
	
	
	
	
	
	
	
	
	