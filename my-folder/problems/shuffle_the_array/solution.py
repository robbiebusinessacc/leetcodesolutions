class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        z=[]
        for i in range(len(nums)//2):
            z.extend([nums[i],nums[i+n]])
        return z