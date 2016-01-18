# --- Introduction ---
"""
	- The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
	rows like this:(you may want to display this pattern in a fixed font better 
	legibility)
	:
		P   A   H   N
		A P L S I I G
		Y   I   R
	- And then read line by line: "PAHNAPLSIIGYIR"
	- Write the code that will take a str and make this conversion given a number of
	rows.
	- string convert(string text, int nRows);
	- convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

# --- Code ---
"""
	Δ=2n-2    1                           2n-1                         4n-3
	Δ=        2                     2n-2  2n                    4n-4   4n-2
	Δ=        3               2n-3        2n+1              4n-5       .
	Δ=        .           .               .               .            .
	Δ=        .       n+2                 .           3n               .
	Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
	Δ=2n-2    n                           3n-2                         5n-4

	- The idea is to use the remainder (index%period) to determine which the character
	at the given index will be. The period is calculated first based on nRows. A
	Dictionary with remainder:line as key: value is then created(this can also be done
	with a list or a tuple). Once these are done, we simply go through s, assign each 
	character to its new line, and then combine these lines to get the converted str.
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
		if nRows == 1:
			return s
		period = 2*(numRows - 1)
		lines = ["" for i in xrange(numRows)]
		# d is the dict of the index order.
		d = {}
		for i in xrange(period):
			if i < numRows:
				d[i] = i
			else:
				d[i] = period - i
		
		for i in xrange(len(s)):
			lines[d[i%period]] += s[i]
		
		return "".join(lines)
		