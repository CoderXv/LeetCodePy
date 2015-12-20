# --- Introduction ---
"""
	- Find the total area covered by two rectilinear rectangles in a 2D plaen.
	- Each rectangle is defined by its bottom left corner and top right corner as
	shown in the figure.
	- Assume that the total area is never beyond the maximum possible value of int.
"""

# --- Code ---
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
		# if not overlap the length or the height would be negative, so just set it as 0
		overlap = max(min(C, G)-max(A, E), 0)* max(min(D, H)-max(B, F), 0)
		return (A-C)*(B-D) + (E-H)*(F-H) - overlap