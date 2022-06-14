class Solution:
	def totalMoney(self,n):
		a=1;total=0
		while n>7:total+=3.5*(2*a+6);a+=1;n=n-7
		if n!=0:total+=n/2*(2*a+(n-1))
		return int(total)