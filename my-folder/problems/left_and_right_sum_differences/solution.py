class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left,right = 0,sum(nums)      
        for i,num in enumerate(nums):                    
            left+=num                  
            nums[i]=abs(right-left)
            right-=num
        return nums