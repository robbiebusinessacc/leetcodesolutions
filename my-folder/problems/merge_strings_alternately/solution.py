class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=""
        z=min(len(word1),len(word2))
        for x,y in zip(word1,word2):
            if x and y:k+=x+y
        return k+word1[z:]+word2[z:]