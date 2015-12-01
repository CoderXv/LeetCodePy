# --- Introduction ---
"""
	- Given a binary tree:
		struct TreeLinkNode {
		  TreeLinkNode *left;
		  TreeLinkNode *right;
		  TreeLinkNode *next;
		}
	- Populate each next pointer to point to its next right node. If there is no next
	right node, the next pointer should be set to null.
	- Initially, all next pointers are set to null.
	- Note:
		You may only use constant extra space.
		You may assume that it's a perfect binary tree(ie, all leaves are the same level
		, and every parent has two children.)
"""

# --- Code ---
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
		if root == None:
			return 
		present = root
		current = None
		while(present.left):
			current = present
			while(current):
				current.left.next = current.right
				if current.next:
					current.right.next = current.next.left
				current = current.next
			present = present.left
	