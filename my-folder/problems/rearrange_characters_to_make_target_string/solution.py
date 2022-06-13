class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return min(Counter(s)[c]//d for c,d in Counter(target).items())