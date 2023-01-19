class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        count = [0]*k
        count[0] = 1
        for num in nums:
            cur_sum += num
            mod_idx = cur_sum % k
            if mod_idx < 0:
                mod_idx += k
            res += count[mod_idx]
            count[mod_idx] += 1
        return res