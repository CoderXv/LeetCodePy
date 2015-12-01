# --- Introduction ---
"""
	- Given an array where elements are sorted in ascending order, convert it to a
	height balanced BST.
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
		if not nums:
			return None
		else:
			return self.buildBST(nums, 0, len(nums)-1)
	
	def buildBST(self, list, start, end):
		if start > end:
			return None
		mid = start + (end - start) / 2
		node =  TreeNode(mid)
		node.left = self.build(list, start, mid-1)
		node.right = self.build(list, mid+1, end)
		return node