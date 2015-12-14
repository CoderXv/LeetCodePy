# --- introduction ---
"""
	Given a sorted linked list, delete all duplicates such that each element appear
	only once.
	For example, 
	Given 1->1->2, return 1->2;
	Given 1->1->1->1->2->3->3, return 1->2->3.
"""


# --- Solution ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# need to notice that its a sorted linked list !
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
		current = head
		while current:
			while current.next and current.val == current.next.val:
				current.next = current.next.next
			current = current.next
		return head
