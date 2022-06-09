class Solution:
	def isSymmetric(self,root):
		def A(root1,root2):
			if not root1 and not root2:return True
			if not root1 or not root2:return False
			return root1.val==root2.val and A(root1.right,root2.left)and A(root1.left,root2.right)
		return A(root,root)