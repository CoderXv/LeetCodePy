# --- Introduction ---
"""
	- Merge k sorted linked lists and return it as one sorted list.
	- E.G:
	- Input [[0], [1, 3, 4, 5], [1, 3, 4, -1, 5]]
	- Output [-1, 0, 1, 1, 3, 3, 4, 4, 5, 5]
"""

# --- Brief Solution ---
"""
	- Learn from merge sort in arrays, we can conclude a solution:
	- parse all the head-node in the list then merge them one by one, each time we 
	return the head-node of the new list, then use it to merge with the next node.
	- This algorithm is low efficient, it has run out of the time resources. 
	- To optimize this algorithm, we can use recursion and divide and conquer.
	- Firstly, we divide all of the head-node-in-lists in to individual ones, then merge
	them in pairs, E.G: we merge the 1st with 2nd, 3rd with 4th, and vice versa, until 
	we get the intergrated one.
	- so the return edge in the recursion is to detect the len of sub-list is 1 or zero,
	if it's satisfied, then stop dividing and start merging. 
""" 

# --- Program ---
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if not lists:
			return None
		elif len(lists) == 1:
			return lists[0]
		else:
			mid = len(lists) / 2
			left_header = self.mergeKLists(lists[:mid])
			right_header = self.mergeKLists(lists[mid:])
			
			sentiel = ListNode(0)
			current = sentiel
			
			while left_header and right_header:
				if left_header.val > right_header.val:
					current.next = right_header
					right_header = right_header.next
				else:
					current.next = left_header
					left_header = left_header.next
				current = current.next
			
			if left_header:
				current.next = left_header
			else:
				current.next = right_header
			
			return sentiel.next

# --- below is the original low-efficient case:
"""
:Low - efficient
:Failed Reason: Time limited, cosuming too much resources.

class Solution(object):
    
    def mergeKLists(self, lists):        
        # The return value is the head listNode of the whole list.
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            list_len = len(lists)
            index = 1
            dummy_header = lists[0]
            while index < list_len:
                dummy_header = self.merge_node(dummy_header, lists[index])
                index += 1
            return dummy_header
            
    def merge_node(self, node1, node2):
        if not node1:
            return node2
        elif not node2:
            return node1
            
        if node1.val < node2.val:
            dummy_header = node1
            node1 = node1.next
        else:
            dummy_header = node2
            node2 = node2.next
        start_node = dummy_header
        while (node1 and node2):
            if node1.val > node2.val:
                dummy_header.next = node2
                dummy_header = dummy_header.next
                node2 = node2.next
            else:
                dummy_header.next = node1
                dummy_header = dummy_header.next
                node1 = node1.next
        if node1:
            dummy_header.next = node1
        else:
            dummy_header.next = node2
        return dummy_header
"""  
