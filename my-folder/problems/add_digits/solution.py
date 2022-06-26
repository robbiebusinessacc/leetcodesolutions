class Solution:
    def addDigits(self,num):
        while len(str(num))>1:
            sum=0
            for digit in str(num):
                sum+=int(digit)
            num=sum
        return num
    
