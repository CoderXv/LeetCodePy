# --- Introduction --- 
"""
	Given a linked list, remove the n-th node from the end of list and return its end.
	E.G:
		- Given linked list: 1-2-3-4-5, and n = 2
		- After removing the second node from the end, the linked list becomes 1-2-3-5
	Note:
		- Given n will always be valid.
		- Try to do this in one pass.
"""

# --- Code ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
		# two pointer.
		h1, h2 = head, head
		for i in xrange(n):
			h2 = h2.next 
		if h2 == None:
			# the head is the target.
			return head.next
		h2 = h2.next
		while h2:
			h1 = h1.next
			h2 = h2.next
		h1.next = h1.next.next
		return head