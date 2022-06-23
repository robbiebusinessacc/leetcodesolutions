class Solution:
    def divide(self, dividend,divisor):
        return min(int(str(dividend/divisor).split('.')[0]),2**31-1) 
        
