# --- Introduction ---
"""
	- You are climbing a stair case. It takes n steps to reach the top.
	- Each tiem you can either climb 1 or 2 steps. In how many distinct ways can you 
	climb to the top?	
"""

# --- Solution Introduction ---
"""
	- The problem seems to be a dynamic programming one. Hint: the tag also suggest that!
	- Here are the steps to get the solution incrementally.
	- Base cases:
	- if n <= 0, then the number of ways should be zero. if n == 1, then there's only 
	way to climb the stair, if n == 2, then there are two ways to climb the stairs. One
	solution is one stop by another, the other one is two steps at one time.
	- The key intuition to slove the problem is that given a number of stairs n, if we 
	know the number ways to the points [n-1] and [n-2] respectively, denote as n1 and n2
	, then the total ways to the points to get to the point [n] is n1 + n2. Because from
	the [n-1] point, we can take one single step to reach [n]. And from the [n-2] point,
	we could take two steps to get there. There is no overlapping between these two
	solution sets, because we differ in the final step.
	- Now given the above intuition, one can construct and array where each node stores
	the solution for each number n. Or if we look at it closer, it is clear that this is
	basically a fibonacci number, with the starting numbers as 1 and 2, instead of 1
	and 1.
	- Fibonnaci Array:
	F(n) = F(n-1) and F(n-2) n > 2 and n is int.
"""

# --- Code ---
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
		if n == 0:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 2
		index = 2
		one_step_before = 2
		two_step_before = 1
		all_ways = 0
		while index < n:
			all_ways = one_step_before + two_step_before
			two_step_before = one_step_before
			one_step_before = all_ways
			index += 1
			
		return all_ways
