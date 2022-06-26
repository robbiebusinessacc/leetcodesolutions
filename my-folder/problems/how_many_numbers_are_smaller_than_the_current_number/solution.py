class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            s=0
            for othernum in nums:
                if num > othernum:s+=1
            ans.append(s)
        return ans