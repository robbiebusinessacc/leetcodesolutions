class Solution:
    def firstUniqChar(self, s: str) -> int:
        index=[s.index(l) for l in 'abcdefghijklmnopqrstuvwxyz' if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1