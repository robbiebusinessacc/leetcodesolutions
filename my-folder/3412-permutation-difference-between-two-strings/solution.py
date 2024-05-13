class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i-t.index(x)) for i,x in enumerate(s))
