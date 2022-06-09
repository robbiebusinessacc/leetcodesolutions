class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        s=s[-1]
        return(len(s))
        