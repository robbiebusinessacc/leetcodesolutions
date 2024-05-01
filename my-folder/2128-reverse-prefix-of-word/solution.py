class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            z=word.split(ch)
            prefix=ch+z[0][::-1]
            z.remove(z[0])
            return prefix+ch.join(z)
        return word
