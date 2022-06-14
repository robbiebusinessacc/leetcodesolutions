class Solution:
    def firstPalindrome(self, words):
        for l in words:
            if l==l[::-1]:return(l)
        return("")