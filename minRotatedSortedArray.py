# --- Introduction ---
"""
	- Find Minimum in Rotated Sorted Array
	- Suppose a sorted array is rotated at some pivot unkown to you beforehand.
	- Find the minimum element.
	- You may assume no duplicate exists in the array.
	- Tag: Array, Binary Search
"""


# --- Code ---

# iteratively
class Solution(object):
	def findMin(self, nums):		
		"""
		:type nums: List[int]
		:rtype: int 
		"""
		min = 0
		max = len(nums) - 1
		while max > min:
			mid = min + (max - min) / 2
			if nums[mid] > nums[max]:
				min = mid + 1
			else:
				max = mid 
		return nums[min]
	
# recursively
class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int 
		"""
		return self.binary(nums, 0, len(nums)-1)
	
	def binary(self, nums, min, max):
		if min == max:
			return nums[min]
		mid = (max + min) / 2
		if nums[max] > nums[mid]:
			return self.binary(nums, min, mid)
		else:
			return self.binary(nums, mid+1, max)
			
	
