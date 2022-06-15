class Solution:
	def arraySign(self,nums):
		if 0 in nums:return 0
		ans=1
		for num in nums:
			if num<0:ans=-ans
		return ans