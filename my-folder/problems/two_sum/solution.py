class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
             for w in nums:
                    if num+num==target and nums.count(num)>1:
                        z=nums.index(num)
                        l=nums
                        i = l.index(num)
                        l = l[:i]+['_']+l[i+1:]
                        nums=l
                        print(nums.index(num),nums)
                        return([z,nums.index(num)])
                    if w+num==target and w!=num:
                        return([nums.index(num),nums.index(w)])