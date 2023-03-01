class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            while left and right:
                res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
            return res + left + right
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
            return merge(left, right)
        
        return merge_sort(nums)
