class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len([0 for l in set(word.lower()) if l.upper() in word and l in word])
