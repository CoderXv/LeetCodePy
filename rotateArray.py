# --- Introduction ---
"""
	- Rotate an array of n elements to the right by k steps.
	- For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to 
	[5,6,7,1,2,3,4].
	- Note:
	- Try to come up as many solutions as you can, there are at least 3 different ways
	to slove this problem.
"""


# --- Code ---
# --- Method 1 ---
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		if not nums:
			return
		k %= len(nums)
		nums.reverse()
		self.reverse(nums, 0, k-1)
		self.reverse(nums, k, len(nums)-1)
	def reverse(self, nums, begin, end):
		while(begin < end):
			nums[begin], nums[end] = nums[end], nums[begin]
			end -=1
			begin += 1
			
# --- Method 2 ---
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
		
# --- Method 3 ---
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		if len(nums) < 1:
			return
		while k > 0:
			nums.insert(0, nums.pop())
			k -= 1