class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        return min((ni + nj + nk for ni, nj, nk in zip(list(accumulate(nums, func = min)), nums[1:-1], list(accumulate(nums[::-1], func = min))[-3::-1])if (ni < nj > nk)), default=-1)