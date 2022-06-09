class Solution:
	def jump(self,nums):
		C=0;R=0;jump=0
		for (i,j) in enumerate(nums):
			if i>R:return-1
			if i>C:jump+=1;C=R
			R=max(R,i+j)
		return jump