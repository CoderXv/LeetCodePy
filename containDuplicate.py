# --- Contains Duplicate I ---
"""
	- Given an array of integers, find if the array contains any duplicates. Your 
	function should return true if any value appears at least twice in the array, and 
	it should return false if every element is distinct.
"""

# --- Code ---
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
		if len(nums) <= 1:
			return Flase
		nums.sort()
		sentinel = 1
		while sentinel <= len(nums)-1:
			if nums[sentinel-1] == nums[sentinel]:
				return True
			sentinel += 1
		return False
		

# --- Contains Duplicate II ---
"""
	- Given an array of integers and an integer k, find out whether there are two 
	distinct indices i and j in the array such that nums[i] = nums[j] and the 
	difference between i and j is at most k.
"""

# --- Code ---
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
		# the difference between i and j is at most k.
		# Never forget dictionary in python.
		ref = {}
		# method to getting the index and obj at the same time.
		for i, v in enumerate():
			if v in ref and i - ref[v] <= k:
				return True
			else:
				ref[v] = i
		return False
		
# --- Contains Duplicate III ---
"""
	- Given an array of integers, find out whether there are two distinct indices i 
	and j in the array such that the difference between nums[i] and nums[j] is at 
	most t and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
		# condition:
		# nums[i] - nums[j] <= t
		# i - j < = k 
		# bucket sorting. BST. hash table
		if t < 0:
			return False
		n = len(nums)
		d = {}
		# t is the window length.
		t += 1
		for i in xrange(n):
			if i > k:
				# keep the ref is the content of the current window.
				del d[nums[i - k - 1] / t]
			m = nums[i] / t
			if m in d:
				return True 
			if m - 1 in d and abs(nums[i] - d[m - 1]) < t:
				return True
			if m + 1 in d and abs(nums[i] - d[m + 1]) < t:
				return True
			# store the current index
			d[m] = nums[i]
		return False

