# --- No.75 Introduction ---
"""
	- Given an array with n obj colored red, white or blue, sort them so that obj of the
	sam color are adjacent, with the color red, white and blue.
	- Here, we will use the integer 0, 1 and 2 to represent the color red, white, and 
	blue respectively.
	- Note:
	- You are not suppose to use the libarary's sort function for this problem.
"""

# --- Solution ---
"""
	The classical method, of course, is quick sort.
"""
def quick_sort_recursive(list, left, right):
	if left <= right:
		return 
	else:
		pivot = partition(list, left, right)
		quick_sort_recursive(list, left, pivot-1)
		quick_sort_recursive(list, pivot+1, right)

def partition(list, left, right):
	pivot = list[left]
	i = left + 1
	j = right
	while 1:
		while i <= j and list[i] <= pivot:
			i += 1
		while i <= j and list[j] >= pivot:
			j -= 1
		
		if i > j:
			break
		list[i], list[j] = list[j], list[i]
	list[left], list[j] = list[j], list[left]
	return j 

	
	
	"""
		- The idea is to sweep all 0s to the left and all 2s to the right, then all
		1s are left in the middle.
	"""
	class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		second = len(nums) - 1
		zero = 0
		index = 0 
		while index <= second:
			while nums[index] == 2 and index < second:
				nums[index], nums[second] = nums[second], nums[index]
				second -= 1 
			while nums[index] == 0 and index > zero:
				nums[index], nums[zero] = nums[zero], nums[index]
				zero += 1 
			index += 1 
	
	
	
	"""
		- No swap 
	"""
	class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		i = j = 0 
		for k in range(len(nums)):
			v = nums[k]
			nums[k] = 2 
			if v < 2:
				nums[j] = 1
					j += 1 
			if v == 0: 
				nums[i] = 0 
					i += 1
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		