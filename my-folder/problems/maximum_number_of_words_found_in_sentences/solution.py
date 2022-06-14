class Solution:
    def mostWordsFound(self,sentences):
        return max(len(w.split())for w in sentences)