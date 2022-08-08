class Solution:
	def invertTree(B,root):
		R=root
		if R:R.left,R.right=B.invertTree(R.right),B.invertTree(R.left)
		return R