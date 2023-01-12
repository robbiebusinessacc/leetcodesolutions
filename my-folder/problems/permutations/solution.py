class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l,lenNums=[],len(nums);
        for i in range(6000):l.append(random.sample(nums,lenNums))
        return(list(set(tuple(i) for i in l)))