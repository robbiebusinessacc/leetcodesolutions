class Solution:
    def pivotInteger(self, n: int) -> int:
        x = (n*(n+1)/2)**0.5
        return int(x) if int(x) == x else -1
