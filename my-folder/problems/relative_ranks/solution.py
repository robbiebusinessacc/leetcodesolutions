class Solution:
    def findRelativeRanks(self,nums):
        return list(map(dict(list(zip(sorted(nums)[::-1],['Gold Medal','Silver Medal','Bronze Medal']+list(map(str,list(range(4,len(nums)+1))))))).get,nums))