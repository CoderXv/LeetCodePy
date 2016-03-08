# --- Introduction ---
# 144. Linked List Cycle 
"""	
	Given a linked list, determine if it has a cycle in it.
"""

# --- Code ---
# Given two pointers in the linked list with to iter speed, they will meet sooner or
# later if there's a cycle in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
		try:
			faster = head.next
			slower = head 
			while slower is not faster:
				slower = slower.next
				faster = faster.next
			return True
		except:
			return False 