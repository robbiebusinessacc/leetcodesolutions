class Solution:
	def convertToTitle(self,n):
		r=''
		while n>0:n-=1;r+=chr(n%26+ord('A'));n//=26
		return r[::-1]