# --- Introduction ---
"""
	- You are a professional robber planning to rob houses along a street. Each house 
	has a certain amount of money stashed, the only constraint stopping you from 
	robbing each of them is that adjacent houses have security system connected and it 
	will automatically contact the police if two adjacent houses were broken into on 
	the same night.
"""

# --- Code ---
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        odd = 0
        even = 0
        index = 0
		# It's a dynammic programming problem.
		while index < nums:
			if index % 2 == 0:
			"""
				- At this position, compare with the last time result:
				- if we take the money at this house is better than the result we do at
				last odd position, we take the current strategy as the current best 
				strategy. So do we choose the opposite one.				
			"""
				even = max(odd, even + nums[index])
			else:
				odd = max(even, odd + nums[index])
			index += 1
			
		return max(odd, even)