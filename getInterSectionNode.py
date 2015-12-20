# --- Introduction ---
"""
	- Write a program to find the node at which the intersection of two singly linked
	lists begins.
	- E.G:
	a1 - a2 - c1 - c2 - c3
			  |
	b1 - b2 - b3
	- begin to intersect at node c1.
	Note:
	1.if the two linked lists have no intersection at all, return all.
	2.The linked lists must retain their original structure after the function returns.
	3.You may assume there are no cycle anywhere in the entire linked structure.
	4.Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# --- Code One ---
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
		# get the len of link a and b.
		lena, lenb = 0, 0
		p1, p2 = headA, headB
		
		while p1:
			lena += 1
			p1 = p1.next
			
		while p2:
			lenb += 1
			p2 = p2.next
		
		p1, p2 = headA, headB
		# move p1 or p2 to the same position (ref to the end of the list.)
		if lena > lenb:
			for i in xrange(lena-lenb):
				p1 = p1.next
		elif lena < lenb:
			for i in xrange(lenb-lena):
				p2 = p2.next
		
		while p1 != p2:
			p1 = p1.next
			p2 = p2.next
		# now condition is p1 = p2 or p1 = None and p2 = None
		return p1
		
# --- Code Two ---
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """	
		if not headA or headB:
			return None
		
		p1 = headA
		p2 = headB
		# if either pointer hits the end, switch head and continue the second 
		# traversal,
		# if not hit the end, just move on to next.
		while p1 is not p2:
			if p1 is None:
				p1 = headB
			else:
				p1 = p1.next
			
			if p2 is None:
				p2 = headA
			else:
				p2 = p2.next
		return p1
		# the idea is if you switch head, the possible difference between length
		# would be countered.
		# On the second traversal, they either hit or miss.
		# if they meet, p1 or p2 would be the node we are looking for.
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		