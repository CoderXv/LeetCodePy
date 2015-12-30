# --- Introduction ---
"""
	- Given two strings s and t, determine if they are iosmorphic.
	- Two strings are isomorphic if the characters in s can be replaced to get t.
	- All occurences of a character must be replaced with another character while
	preserving the order of characters. No two characters may map to the same character
	but a character may map to itself.
	- E.G:
		Given "egg", "add", return true.
		Given "foo", "bar", return false.
		Given "paper", "title", return true.
	- Isomorphic:
	- Isomorphic is a very general concept that appears in several areas of mathematics.
	The word derives from the Greek iso, meaning "equal", and morphosis, meaning "to 
	form" or "to shape".
"""

# --- New Bulit-In Method ---
"""
	- zip([iterable, ...])
	- This function returns a list of tuples, where the i-th tuple contains the i-th
	element from each of the argument sequences or iterables. The returned list is
	truncated in length to the length of the shortest argument sequence. When there are
	multiple arguments which are all of the same length, zip() is similar to map() with
	an initial argument of None. With a single sequence argument, it returns a list of
	l-tuples. With no arguments, it returns an empty list.
	- E.G:
		>>> x = [1, 2, 3]
		>>> y = [4, 5, 6]
		>>> zipped = zip(x, y)
		>>> zipped
		>>> [(1, 4), (2, 5), (3, 6)]	
"""

# --- Code ---
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
		return len(set(zip(s, t))) == len(set(s, t)) == len(set(s, t))
		