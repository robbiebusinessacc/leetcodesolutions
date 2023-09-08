class Solution:
    def countSymmetricIntegers(self, i: int, high: int) -> int:
        count=0
        
        while i<high+1:
            digits = len(str(i))
            if digits%2==0:
                if sum([int(x) for x in str(i)[:digits//2]]) == sum([int(x) for x in str(i)[::-1][:digits//2]]):
                    count+=1
            else:
                i=10**(digits)
            i+=1
        return(count)