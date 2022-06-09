class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a=-110000
        for l in nums:
            #print(a,l)
            if abs(l)-0<abs(a)-0:
                if abs(a)==abs(l):
                    a=abs(l)
                else:
                    a=l
            if abs(l)==abs(a) and l!=a:
                a=abs(l)
        return(a)