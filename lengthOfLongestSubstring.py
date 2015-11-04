# --- Introduction ---
"""
	- Given a string, find the length of the longest substring without repeating 
	characters. E.G:
	- The longest substring without repeating letters for "abcabcbb" is "abc", which the
	length is 3. For "bbbb" the longest substring is "b", with the length of 1.
"""

# --- Brief Solution ---
"""
	- The point of this question is to locate the edge of the substring.
	- For example the "dvdf": 
	- When we parse the string, the first substring is d, then dv, vd, vdf, so the 
	biggest one is 3. so how can we locate the left edge of substring?
	- The answer is to when we find the repeated char, we move the left pointer to the 
	next pos of to the latest pos of repeated char. E.G:
	- if "dvdf", when we find the next d, we move left-pointer to the v;
	- if "dvddf", when we find the 2nd d, we move the left one to the char v, then we 
	move the pointer to the 3rd d, the next pos of the 2nd char d, the current
	substring is "d" at the same time.
	- Room we allocate:
	- For all the char in the string, the 8 bits character in asicii is ranges from 
	0 to 255, need 256 element in the list. each one stores the latest index where this
	char shown. all of spaces can init with number -1.
"""

# --- Code ---
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            maxLen = 0
            curLen = 0
            start = 0
            index = 0
            # init a table for store the index of the char appearing in the string.
            # 8 bit char range from 0 to 255, so we need 256 list to store.
            lastIndices = [-1] * 256
            # parse each char.
            while index < len(s):
                cur = s[index]
                # the first time for a char appearing in the string. 
                if(lastIndices[ord(cur)] < start):
                    # store the index of this char 
                    lastIndices[ord(cur)] = index
                    # cause this is a new char, so the curLen ++
                    curLen += 1
                else:
                    # This char has shown before.
                    # The lastest pos this char has appeared.
                    lastIndex = lastIndices[ord(cur)]
                    # move the start pos to the next one after the its latest occurance.
                    # cause the interval from this position to the cur-Index, all of char are unique.
                    start = lastIndex+1
                    # calculate the new sub-string length 
                    curLen = index - start+1
                    lastIndices[ord(cur)] = index
                # check the curLen is the max one or
                if curLen > maxLen:
                    maxLen = curLen
                index += 1
            return maxLen