# --- Introduction ---
"""
	- Given an array of integers, find two numbers such that they add up to a specific
	target number.
	- The function twoSum should return indices of the two numbers such that they add
	up to the target, where index1 must be less than index2. Please note that your
	returned answers(both index1 and index2) are not zero-based.
	- you may assue that each input would have exactly one solution.
	- Input: numbers = {2, 7, 11, 15}, target = 9
	- Output: index1 = 1, index2 = 2
"""

# --- Brief Solution ---
"""
	- At first we can come up with an algorithm: 
	- First we can come up with a new idea:
	- for item , i to range(len(nums)):
		for item1, j to range(len(nums)):
			if item + item1 == target:
				return (i+1, j+1)
	- This algorithm is okay, but it's very low-efficient.
	- To optimize it. if there's only one match, we can make a dict to store the
	result z = x + y. such as d["3"] = 4, target is 7. 
"""

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		d = {}
		for figure, index in nums:
			if d.has_key(index):
				return (d[index]+1, figure+1)
			else:
				d[target-index] = figure.
		return (0, 0)