# --- Introduction ---
"""
	- You are given two linked lists representing two non-negative numbers. The digits are
	stored in reverse order and each of their nodes contain a single digit. Add the two
	numbers and return it as a linked list.
	- Input: (2->4->3) + (5->6->4)
	- Output: 7->0->8
"""

# --- Code ---
"""
Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
"""

class Solution(object):
	def addTwoNumbers(self, l1, l2):
	"""
	:type l1: ListNode
	:type l2: ListNode
	:rtype: ListNode
	"""
	if not l1:
		return l2
	elif not l2:
		return l1
	
	carry = 0
	dummy_head = ListNode(0)
	current = dummy_head
	
	while l1 and l2:
		temp = l1.val + l2.val + carry
		l1 = l1.next
		l2 = l2.next
		carry = temp / 10
		current.next = ListNode(temp - 10*carry)
		current = current.next
	
	while l1:
		temp = l1.val + carry
		l1 = l1.next
		carry = temp / 10
		current.next = ListNode(temp - 10*carry)
		current = current.next
	
	while l2:
		temp = l2.val + carry
		l2 = l2.next
		carry = temp / 10
		current.next = ListNode(temp - 10*carry)
		current = current.next
	if carry == 1:
		current.next = ListNode(1)
	
	return dummy_head.next