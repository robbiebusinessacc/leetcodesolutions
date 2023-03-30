class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(set(nums))[-3]if len(set(nums))>2 else max(nums)
        
        