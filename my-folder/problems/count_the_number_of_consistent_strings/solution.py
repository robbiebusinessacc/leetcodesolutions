class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum([1for word in words if[1for letter in word if letter not in allowed]==[]])