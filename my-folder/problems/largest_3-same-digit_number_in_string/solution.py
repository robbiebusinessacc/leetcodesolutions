class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(10):
            if str(9-i)*3 in num:return str(9-i)*3
        return ''