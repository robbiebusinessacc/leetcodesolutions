class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(1for i,j in combinations(nums,2)if i==j)