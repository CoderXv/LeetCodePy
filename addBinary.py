# --- Introduction ---
"""
	- Given two binary strings, return their sum (also a binary string).
	- For example:
	- a = "11"
	  b = "1"
	  return  "100"
"""

# --- Code ---
class Solution(object):
	def addBinary(self, a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	len_a = len(a) - 1
	len_b = len(b) - 1
	temp = []
	result = []
	carry = 0
	while len_a >= 0 and len_b >= 0:
		sum = int(a[len_a]) + int(b[len_b]) + carry
		if sum == 2:
			sum = 0 
			carry = 1
		elif sum == 3:
			sum =1
			carry = 1 
		else:
			carry = 0
		temp.append(str(sum))
		len_a -= 1
		len_b -= 1 
		
	while len_a >= 0:
		sum = int(a[len_a]) + carry
		if sum == 2:
			carry = 1 
			sum = 0
		elif sum == 3:
			carry = 1
			sum = 1 
		else:
			carry = 0
		temp.append(str(sum))
		len_a -= 1 
	
	while len_b >= 0:
		sum = int(b[len_b]) + carry
		if sum == 2:
			carry = 1
			sum = 0
		elif sum == 3:
			carry = 1 
			sum = 1
		else:
			carry = 0
		temp.append(str(sum))
		len_b -= 1
	
	if carry == 1:
		temp.append(str(1))
	
	while temp:
		result.append(temp.pop())
	result1 = ''.join(result)
	
	return result1
			