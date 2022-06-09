class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return(nums.index(target))
        else:
            for thing in nums:
                if int(thing)>int(target):
                    return(nums.index(thing))
            return(len(nums))