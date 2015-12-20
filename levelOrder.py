# --- Introduction ---
"""
	- Given a binary tree, return the level order traversal of its nodes' values.
	(ie, from left to right, level by level.)
	E.g: 
	input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
	output: [[1],[2,3],[4,5,6,7],[8,9]]
	Tags: Tree, Breadth-first Search.
"""

# --- Code ---
"""
	- It's a bfs search ,we need two list, one for store the total result list, another
	for store the nodes in current layer. for each node's child, node.left and
	node.right, we can create a temp list to store it and then change it into list we 
	store nodes of the layer.
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, cur = [], [root]
		
		while root and cur:
			res.append([node.val for node in cur])
			# move to next layer, store the next layer's nodes in pair 
			leaf = [(node.left, node.right) for node in cur]
			# change the nodes' format and store.
			# pair is (node.left, node.right)
			cur = [node for pair in leaf for node in pair if node]
		
		return res