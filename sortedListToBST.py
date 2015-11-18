# --- Introduction ---
"""
	- Given a singly linked list where elements are sorted in ascending order, covert 
	it to a height balanced BST.
"""

# --- Point ---
"""
	- change the linked list to array then build it recursively.
"""

# --- Code ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head:ListNode
		:rtype: TreeNode
		"""
		if head == None:
			return None
		
		figureList = []
		
		while head:
			figureList.append(head.val)
			head = head.next
		
		return self.buildBST(figureList, 0, len(figureList)-1)

	def buildBST(self, list, start, end):
		if start > end:
			return None
		mid = start + (end - start) / 2
		node = TreeNode(list[mid])
		node.left = self.buildBST(list, start, mid-1)
		node.right = self.buildBST(list, mid+1, end)
		return node