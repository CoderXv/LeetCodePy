# --- 216.CombinationSum3 ---
# --- Introduction ---
"""
	- Find all purpose combinations of k numbers that add up to a number n, given that 
	only numbers from 1 to 9 can be used and each combination should be a unique set of
	numbers.
	- Ensure that numbers within the set are sorted in ascending order.
	- Example:
	- Input: k = 3, n = 7
		Output:[[1,2,4]]
	- Input: k = 3, n = 9
		Output:[[1,2,6], [1,3,5], [2,3,4]]
"""

# --- Code ---
"""
	Cause it's ascending order, the first round is 1...9 then the second round is 2...9, details depend on value of first round.
	depends on the previous number.it's also like a tree structure, so we can use dfs
	recursive here. The edge condition is that we should return while length of sublist
	is larger than 9 or current value is larger than 9.
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
		result = []
		self.helper(1, n, k, [], result)
		return result
	
	def helper(self, sentinel, total, length, sublist, result):
		# edge condition
		# match
		if len(sublist) == length:
			if sum(sublist) == total:
				result.append(list(sublist))
			return 
		# not match
		if len(sublist) > length or sentinel > 0:
			return 
		
		# parse all the possbile value at this point.
		for i in range(sentinel, 10):
			sublist.append(i)
			self.helper(i+1, total, length, sublist, result)
			sublist.pop()
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
		
