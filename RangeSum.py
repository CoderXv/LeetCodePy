# --- Introdution ---
"""
	- Given an integer array nums, find the sum of the elements between indices i and 
	j (i ¡Ü j), inclusive.
	- Example:
	- Given nums = [-2, 0, 3, -5, 2, -1]	
		sumRange(0, 2) -> 1
		sumRange(2, 5) -> -1
		sumRange(0, 5) -> -3
	- Time limits, must be dynamic programming.
"""

# --- Code ---
# the init function creates a list to store the sum of nums[]
# nums[i] + .... + nums[0] = list[i]
# sumrange = list[j+1] - list[i]
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
		self.sums = [0]
		for num in nums:
			self.sums.append(self.sums[-1] + num)
		
    def sumRange(self, i, j):
        sum = 0
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """	  
		return self.sums[j+1] - self.sums[i] 
		
		
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)