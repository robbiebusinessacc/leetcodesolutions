class Solution:
    def isHappy(self,n):
        A=set()
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])
            if n in A:return False
            else:A.add(n)
        else:return True