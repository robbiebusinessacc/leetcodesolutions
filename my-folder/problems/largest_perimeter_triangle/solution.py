class Solution:
    def largestPerimeter(self, nums):
        nums=sorted(nums)[::-1]
        for i in range(len(nums)-2):
            base,sidea,sideb=nums[i],nums[i+1],nums[i+2] 
            if sidea+sideb>base:return sidea+sideb+base
        return 0