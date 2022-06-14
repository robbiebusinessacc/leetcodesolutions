class Solution:
    def subtractProductAndSum(self,n):
        import math;n=[int(x) for x in str(n)];return math.prod(list(n))-sum(list(n))