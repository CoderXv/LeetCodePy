# --- Introduction ---
"""
	- Reverse bits of a given 32 bits unsigned integer.
	- For example, given input 43261596 (represented in binary as 
	00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).	
"""

# --- Code ---
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
		# This answer demostrates some basic tech in py for bit computing.
		ans = 0
		for i in xrange(32):
		# int n in less than 32 bits.
			ans = (ans << 1) + (n & 1)
			# >> and << is right/left shift in python.
			n >>= 1
		return ans

		
# --- Code2 ---
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
		# we use zfill:
		# zfill(width) pads strings on the left with zero to fill width.
		# para: width -- This is final width of the string. This is the width which we
		# could get after filling zeros.
		# to invert a string: stringname[::-1]
		return int(bin(n)[2:].zfill(32)[::-1],2)
		# convert binary string to decimal figure, int(string, 2)
		