# --- No.48 Rotate Image ---
"""
	- You are given an n * n 2D matrix representing an image.
	- Rotate the image by 90 degrees(clockwise)
"""

# --- Code ---
# classical method 
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
		matrix.reverse()
		for i in range(len(matrix)):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

				
# --- What's more ---
# anti-clockwise rotate 
# firste reverse left to right, then swap the symmetry 
"""
	void anti_rotate(vector<vector<int>> &matrix){\
		for (auto vi: matrix) reverse(vi.begin(), vi.end());
		for (int i = 0; i < matrix.size(); ++i){
			for (int j = i; j < matrix[i].size(); ++j)
				swap(matrix[i][j], matrix[j][i])
		}
	}
"""