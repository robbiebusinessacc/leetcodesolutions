class Solution:
	def lengthOfLIS(self,nums):
		A=[nums.pop(0)]
		for B in nums:
			if B>A[-1]:A.append(B)
			else:A[bisect_left(A,B)]=B
		return len(A)