# --- Introduction ---
"""
	- Given two sorted integer arrays nums1 and nums2, merge num2 into nums1 as one sorted
	array.
	- Note: You may assume that nums1 has enough space(size that is greater or equal to
	m + n) to hold additional elements from nums2. The number of elements initialized 
	in nums1 and nums2 are m and n repectively.
"""

# --- Brief Solution ---
"""
	- There's BIF in python using for element inserting into a list.
	- The list is partly sorted in m and n, so we just append rest of it.
"""

# --- Code ---
class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2:
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		int l1_index, l2_index = 0, 0
		for l2_index in range(n):
			while l1_index < m + l2_index and nums1[l1_index] < num2[l2_index]:
				l1_index += 1
			nums1.insert(l1_index, num2[l2_index])
		nums1[l1_index+l2_index-1:] = num2[l2_index+1:]