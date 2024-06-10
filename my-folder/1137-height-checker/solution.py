class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([0 for h1, h2 in zip(heights, sorted(heights))if h1!=h2])
