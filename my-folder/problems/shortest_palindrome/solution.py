class Solution:
	def shortestPalindrome(self,s):
		if s=='':return''
		for i in range(len(s))[::-1]:
			if s[0:i+1]==s[i::-1]:return s[:i:-1]+s