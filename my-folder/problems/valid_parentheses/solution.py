class Solution:
	def isValid(self,s):
		A=False;z=[];dict={']':'[','}':'{',')':'('}
		for char in s:
			if char in dict.values():z.append(char)
			elif char in dict.keys():
				if z==[]or dict[char]!=z.pop():return A
			else:return A
		return z==[]