# --- Introduction ---
"""
	- Count the number of prime numbers less than a non-negative number, n
	- Hint:
		- parse all the int less than n -> complexity: O(n^2)
		- optimize: 
		the prime number must not be divisible by any number > n/2,so we can
		cut the iteration up to n/2.
		- optimize: We only to consider factors up to sqrt(n), 
		if n is divisible by some
		number p, then n = P * q and since p <= q, we could derive that p <= sqrt(n),
		   -> complexity: O(n^1.5)
		- optimize: Sieve of Eratosthenes complexity: 
		   -> complexity: O(n*loglog(n))
		   for more infomation, please check the wiki for detail.
"""

# --- Solution in Brief ---
"""
	Sieve of Eratosthenes:
	Input: an integer n > 1
	
	Let A be an array of Boolean values, indexed by integers 2 to n,
	initially all set to True.
	for i = 2, 3, 4, ... , not exceeding sqrt(n):
		if A[i] is True:
			for j = i^2, i^2+i, i^2+2*i, ..., not exceeding n:
				A[j] = False
				
	Output: all i such that A[i] is True.	
"""

# --- Program ---
import math 
class Solution(object):
	"""
	: type n: int
	: rtype : int
	"""
	def countPrimes(self, n):
		if n < = 1:
			return 0
		else:
			test_list = [True] * n
			test_list[0] = False
			test_list[1] = True
			index = 2
			sqrt = math.sqrt(n)
			while index < sqrt:
				if test_list[index] = True:
					j = index * index
					while j < n:
						test_list[j] = False
						j += index
				index += 1
		
		prime_count = 0
		for result in test_list:
			if (result):
				prime_count += 1
		return prime_count
		
				