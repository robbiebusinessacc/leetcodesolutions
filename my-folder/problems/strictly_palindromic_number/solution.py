class Solution:
    def numberToBase(n, b):
        if n == 0:return [0]
        d=[]
        while n:
            d.append(int(n%b));n//=b
        return d[::-1]
    def isStrictlyPalindromic(self, n: int) -> bool:
        z=True
        for i in range(2,n-1):
            j=Solution.numberToBase(n,i)
            if j!=j[::-1]:
                z=False
        return z
