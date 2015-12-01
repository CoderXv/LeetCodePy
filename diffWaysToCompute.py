# --- Introduction ---
"""
	- Given a string of numbers and operators, return all possible results from all the
	different possible ways to group numbers and operators.
	- the valid operators are + - and *.
	- Example 1
    - Input: "2-1-1".
		((2-1)-1) = 0
		(2-(1-1)) = 2
	- Output: [0, 2]
	- Example 2
	- Input: "2*3-4*5"
		(2*(3-(4*5))) = -34
		((2*3)-(4*5)) = -14
		((2*(3-4))*5) = -10
		(2*((3-4)*5)) = -10
		(((2*3)-4)*5) = 10
	- Output: [-34, -14, -10, -10, 10]	
"""

# --- Code ---
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
		token = re.split('(\D)', input)
		# seperate the num and the operator from the input str.
		ops = map({'+':operator.add, '-':operator.sub, '*':operator.mul}.get,
		tokens[1::2])
		nums = map(int, token[::2])
		def build(lo, hi):
			return [nums[lo]]
		return [ops[i](a, b) for i in xrange(lo, hi)
							 for a in build(lo, i)
							 for b in build(i+1, hi)]
		return build(0, len(nums)-1)
							 