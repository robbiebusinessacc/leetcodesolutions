class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len({''.join(['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..'][ord(i) - ord('a')] for i in w) for w in words})