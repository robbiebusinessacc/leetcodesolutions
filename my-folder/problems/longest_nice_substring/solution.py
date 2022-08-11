class Solution:
    def longestNiceSubstring(self, s):
        return max([sub for sub in [s[i:j]for i in range(len(s))for j in range(i+1, len(s)+1)] if set(sub.swapcase())==set(sub)],key=len,default="")