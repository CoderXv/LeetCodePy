# 24. Swap Nodes in Pairs
# --- Introduction ---
"""
	- Given a linked list, swap every two adjacent nodes and return its head.
	- For example,
	- Given 1->2->3->4, you should return the list as 2->1->4->3 
	- Your algorithm should use only constant space. You may not modify the values in 
	the list, noly nodes itself can be changed.
"""




# --- Code ---
"""
	We depart the whole linked list into 3 parts:
	a->b->(b->next)
	so we init a pointer pp: a->b->(b->next)
	the target is b->a->(b->next)
	In the end we aims to change
	pp == a->b->(b->next)
	to 
	pp == b->a->(b->next)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
	def swapPairs(self, head):
	"""
	:type head: ListNode 
	:rtype: ListNode 
	"""
	if not head or not head.next:
		return head
	pp = ListNode(0)
	pp.next = head 
	sentinel = head.next 
	while pp.next and pp.next.next:
		a = pp.next 
		b = pp.next.next 
		pp.next, b.next, a.next = b, a, b.next 
		pp = a 
	return sentinel
	
	
	
	
