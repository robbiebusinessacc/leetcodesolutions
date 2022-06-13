class Solution:
	def getLucky(self,s,k):
		s=''.join((str(ord(x)-ord('a')+1)for x in s))
		for i in range(k):s=str(sum((int(x)for x in s)))
		return s