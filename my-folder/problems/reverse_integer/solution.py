class Solution:
	def reverse(self,x):
		sign_multiplier=1
		if x<0:sign_multiplier=-1;x=x*sign_multiplier
		result=0;min_int_32=2**31
		while x>0:
			result=result*10+x%10
			if result*sign_multiplier<=-min_int_32 or result*sign_multiplier>=min_int_32-1:return 0
			x=x//10
		return sign_multiplier*result