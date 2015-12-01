# --- Introduction ---
"""
	- Serialization is the process of converting a data structure or object into a 
	sequence of bits so that it can be stored in a file or memory buffer,  or 
	transmitted across a network connection link to be reconstructed later in the same 
	or another computer environment.
	- Design an algorithm to serialize and deserialize a binary tree. There is no 
	restriction on how your serialization/deserialization algorithm should work. You 
	just need to ensure that a binary tree can be serialized to a string and this 
	string can be deserialized to the original tree structure.
	- Note: Do not use class member/global/static variables to store states. Your 
	serialize and deserialize algorithms should be stateless.
"""

# --- Code ---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
		vals = []
		self.serialize_doit(vals, root)
	
	def serialize_doit(self, vals, root):
		if not root:
			vals.append('#')
		else:
			vals.append(root.val)
			self.serialize_doit(root.left)
			self.serialize_doit(root.right)
			
	def deserialize(self, data):
		if not data:
			return 
		else:
			vals = iter(data.split())
			return self.deserialize_doit(vals)
	
	def deserialize_doit(self, vals):
		val = next(vals)
		if val == '#':
			return None
		node = TreeNode(int(val))
		node.left = self.deserialize_doit(vals)
		node.right = self.deserialize_doit(vals)
		return node
			
			