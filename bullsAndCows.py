# --- Introduction ---
"""
	- Bulls and Cows problem:
	- https://en.wikipedia.org/wiki/Bulls_and_Cows
	- In this question:
	- bulls = digits match secret number exactly in both digits and position.
	- cows = digits match secret number but locate in the wrong place.
	- E.G:
		Secret number:  "1807"
		Friend's guess: "7810"
	- Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
	- We use A to indicate the bulls and B to indicate the cows.
	- Please note that both secret number and friend's guess may contain duplicate 
	digits
"""

# --- New iterator in collections package Introduce --- 
"""
	- A counter is a dict subclass for counting hashable objects. It is an unordered
	collection where elements are sorted as dictionary keys and their counts are stored
	as dictionary values. Counts are allowed to be any integer value including zero or
	negative counts. The counter class is similar to bags or multisets in other laguages
	- details can be found in:
	https://docs.python.org/2/library/collections.html#collections.Counter
	- Common patterns for working with Counter objects:
	sum(c.values())                 # total of all counts
	c.clear()                       # reset all counts
	list(c)                         # list unique elements
	set(c)                          # convert to a set
	dict(c)                         # convert to a regular dictionary
	c.items()                       # convert to a list of (elem, cnt) pairs
	Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
	c.most_common()[:-n-1:-1]       # n least common elements
	c += Counter()                  # remove zero and negative counts
"""

# --- Code ---
import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
		# get two counter iterator.
		s, g = collections.Counter(secret), collections.Counter(guess)		
		bulls = sum(i == j for i , j in zip(secret, guess))
		# find the overlap elements in secret and guess, then del the bulls elements.
		cows = sum((s & g).values()) - bulls
		return "%dA%dB" % (bulls, cows)