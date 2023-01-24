class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(int(a)if i%2==0 else -int(a) for i,a in enumerate(str(n)))