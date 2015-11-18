# --- Introduction ---
"""
	- Given an array S of integers, are there elements a, b, c, and d in S such that a +
	b + c + d = target? Find all unique quadruplets in the array which gives the sum of 
	target.
	- Note:
	- Elements in a quadruplet(a,b,c,d)must be in non-descending order(i.e, a<=b<=c<=d)
	- The solution set must not contain duplicate quadruplets.	
"""

# --- Brief solution --- 
"""
	- from 2 sum to 3 sum and by now we are dealing with 4 sum, we can come up with a 
	universal solution for k sum. all of the k sum problem can be resursively solved by 
	2 sum model. As we can see, cause the array is sorted, so we can use two pointer to remember the index, one start at the head and the other one start at the end. if the result is greater than target, move left pointer, or move the right one.
"""

# --- Code ----
class Solution(object):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""
	def forSum(self, nums, target)
		# use recursive method.
		nums.sort()
		# multi result return.
		results = []
		self.kSum(nums, target, 4, [], results)
		return results
	
	def kSum(self, nums, target, N, result, results):
		# edge detect.
		if len(nums) < N or N < 2:
			return 
		# when it comes to 2 sum then dealing with it.
		elif N == 2:
			l, r = 0, len(nums) - 1
			while l < r:
				if nums[l] + nums[r] == target:
					results.append(result + [nums[l], nums[r]])
					l += 1
					r -= 1
				if nums[l] + nums[r] < target:
					l +=1
				else:
					r -= 1
		else:
			for i in range(0, len(nums)-N+1):
				# check target is in range
				if target < nums[i]*N or target > nums[-1]*N
					break
				# avoid same
				elif i == 0 or i > 0 and  nums[i-1] != nums[i]
					self.kSum(nums[i+1:], target-nums[i], N-1, result+nums[i], results)
		return
			
			