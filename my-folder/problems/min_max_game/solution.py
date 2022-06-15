class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while True:
            cnums=[]
            l=len(nums)
            if l==1:return(nums[0])
            for i in range(l//2):
                if (i+1)%2==0:
                    cnums.append(max([nums[0],nums[1]]))
                else:
                    cnums.append(min([nums[0],nums[1]]))
                nums.remove(nums[0])
                nums.remove(nums[0])
            nums=cnums
            