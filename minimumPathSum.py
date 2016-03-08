# --- No.64 Minimum Path Sum ---
"""
	- Given a m * n grid filled with non-negative numbers, find a path from top left to 
	bottom right which minimizes the sum of all numbers along its path.
	- Note: You can only move either down or right at any point in time.
"""


# --- Solution ---
"""
	- This is a typical DP Problem. Suppose the minimum path sum of arrving at 
	point(i, j) is s[i][j], then the state equation is S[i][j] = min(S[i-1][j], 
	S[i][j-1]) + grid[i][j]. 
	- Well, some boundary conditions need to be handled. The boundary conditions happen
	on the topmost row(S[i-1][j] does not exist) and the leftmost column(S[i][j-1] does
	not exist). Suppose grid is like [1, 1, 1, 1], then the minimum sum to arrive at
	each point is simply an accumulation of previous points and the result is [1,2,3,4]
"""
"""
	- In C++
class Solution{
pubic:
	int minPathSum(vector<vector<int>>& grid){
		int m = grid.size();
		int n = gird.size();
		vector<vector<int>> sum(m, vector<int>(n, gird[0][0]));
		for (int i = 1; i < m: i++)
			sum[i][0] = sum[i-1][0] + grid[i][0];
		for (int j = 1; j < n; j++)
			sum[0][j] = sum[0][j-1] + grid[0][j];
		for (int i = 1; i < m; i++)
			for(int j = 1; j < n; j++)
				sum[i][j] = min(sum[i-1][j], sum[i][j-1]) + grid[i][j];
		return sum[m - 1][n - 1];
	}
}
"""
"""
	- As can be seen, each time when we update sum[i][j], we only need sum[i-1][j]
	(at the current column) and sum[i][j-1](at the left column). So we need not
	maintain the full m*n matrix. Maintaining two columns is enough and now we have
	the following code.
"""

class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype grid: int 
		"""
		m = len(grid)
		n = len(grid[0])
		pre = [grid[0][0]]*m
		cur = [0] * m 
		for j in range(1, n):
			cur[0] = cur[0] + grid[0][j]
			for i in range(1, m):
				cur[i] = min(cur[i-1], pre[i]) + grid[i][j]
			cur, pre = pre, cur
		return cur[-1]
"""
	Further inspecting the above code, it can be seen that maintaining pre is for 
	recovering pre[i], which is simply cur[i] before its update. So it is enough to
	use only one vector. Now the space is further optimized and the code also gets
	shorter.
"""

class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype grid: int 
		"""
		m = len(grid)
		n = len(grid[0])
		cur = [grid[0][0]] * m
		for i in range(1, m):
			cur[i] = cur[i-1] + cur[i][0]
		for j in range(1, n):
			cur[0] += grid[0][j]
			for i in range(1, m):
				cur[i] = min(cur[i], cur[i-1]) + grid[i][j]
		return cur[-1]
				
				
				
				
				
				
				
				
				

