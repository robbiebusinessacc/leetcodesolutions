class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=i=c=0
        while i<len(s):
            if s[i] == 'R':
                r+=1
            else:
                r-=1
            if r==0:
                c+=1
            i+=1
        return c
        