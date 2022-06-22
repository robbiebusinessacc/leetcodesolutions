class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort();return max([abs(nums[i]-nums[i+1])for i in range(len(nums)-1)],default=0)