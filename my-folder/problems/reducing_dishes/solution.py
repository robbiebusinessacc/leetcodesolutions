class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        return max(0,max(itertools.accumulate(itertools.accumulate(sorted(satisfaction,reverse=True)))))