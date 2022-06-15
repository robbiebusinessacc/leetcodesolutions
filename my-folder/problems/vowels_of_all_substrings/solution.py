class Solution:
	def countVowels(self,word):
		vm={'a':1,'e':1,'i':1,'o':1,'u':1};c=0
		for (k,w) in enumerate(word):
			if w in vm:c+=(len(word)-k)*(k+1)
		return c