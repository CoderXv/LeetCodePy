# --- Introduction ---
"""
	Given a singly linked list, determine if it's a plindrome.
	Could you do it in O(n)time and O(1)space?
"""

# --- Code ---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # On time and O1 space.
        # Firstly we move the pointer to the middle of the list
        # then reverse the fllowing part of the list.
        # then we move the head and the middle pointer to compare.
		if not head:
			return True
		
		middle = head
		quick = head 
		if quick.next and quick.next.next:
			middle = middle.next
			quick = quick.next.next
		middle.next = self.reverse(middle.next)
		middle = middle.next
		while middle:
			if middle.val != head.val:
				return False
			else:
				middle = middle.next
				head = head.next
		return True
	
	def reverse(self, head):
		pre = None
		next = None
		if not head:
			return None
		while head:
			next = head.next
			head.next = pre
			pre = head
			head = next
		return pre
		