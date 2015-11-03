# --- Introduction ---
"""
	- Write a program to find the n-th ugly number.
	Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For
	Example, 1, 2, 3, 4, 5, 6, 8, 10, 12 is the sequence of the first 10 ugly numbers.
	Note that 1 is typically treated as an ugly number.
	- Hint:
	- 1. the naive approach is to call isugly for every number until you can reach the 
	n-th one. Most numbers are not ugly. Try to focus on generating only the ugly ones.
	- 2. An ugly number must be multiplied either 2, 3, or 5 from a small ugly number.
	- 3. The key is how to maintain the order of the ugly numbers. Try a similar 
	approach of mergig from three sorted lists: L1, L2, and L3.
	- 4. Assume you have Uk, the k-th ugly number. Then U(k+1) must be min (L1*2, L2*3,
	L3*5)
"""

# --- Brief Solution ---
"""
	- As we can learn from the hint above, we can write a draft:
	- From hint 1 and 2, we can initialize a element as figure 1, then multiply it with 
	2, 3, and 5, trying to find the qualified ugly number.
	- From hint 3 and 4, we can allocate room for storing the previous ugly number, then 
	multiply it with 2, 3, or 5 to find next ugly number till we find the n-th ugly number. So we should define a list, the last element in this list is the n-th ugly
	number we need to find.
"""

# --- Program ---
class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int 
		"""
		ugly = [1]
		index = n
		i2, i3, i5 = 0
		
		while index < 1:
			u2, u3, u5 =  ugly[i2] * 2, ugly[i3] * 3, ugly[5] * 5
			umin = min(u2, u3, u5)
			if umin = u2:
				i2 += 1
			elif umin = u3:
				i3 += 1
			else:
				i5 += 1
				
			ugly.append(umin)
			index -= 1
		
		return ugly[-1] 