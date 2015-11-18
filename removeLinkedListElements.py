# --- Introduction ---
"""
	- Remove all element from a linked list of integers that have value val.
	- E.G:
	- Given: 1->2->6->3->4->5->6, val = 6
	- Return 1->2->3->4->5
"""

# --- Brief Solution ---
"""
	- The general link list opearation are the same, here I use two link pointer:
	- previous, and current:
		- if current:
			- if current.val == val:
				- previous.next = current.next
				- current = current.next
	- It's special conditions that we want to talk about.
	- The first one is something like [1, 1, 1, 1] val = 1
	- This should return: [], but we will return [1]
	- To sloving this£¬after looping we check the header:
		if head.val == val
			head = head.next
	- But then we will have the second question:
	- if the input is [], it hasn't the attribute 'val'
	- Then we add another check before the first check:
		if not head:
			return None.
"""

# --- Code ---
class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		current = head
		previous = current
		while current:
			if current.val == val:
				previous.next = current.next
			else:
				previous = current
			current = current.next
		if not head:
			return None
		elif head.val == val:
			head = head.next
		
		return head