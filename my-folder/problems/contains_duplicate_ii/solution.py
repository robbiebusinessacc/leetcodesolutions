class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):return False
        for i in range(len(nums)):
            if len(nums[i:i+1+k])!=len(set(nums[i:i+1+k])):return True
        return False
                
        