class Solution:
    def minDeletions(self,s):
        D=Counter(s);B=0;C=set()
        for(F,A)in D.items():
            while A>0 and A in C:A-=1;B+=1
            C.add(A)
        return B