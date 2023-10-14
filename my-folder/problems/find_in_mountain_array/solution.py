# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        low,high = 1,length-2
        while low != high:
            mid = low + (high - low) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak_index=low
        increasing_index = self.binary_search(0, peak_index, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index
        decreasing_index = self.binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index

        return -1

    def binary_search(self, low, high, target, mountainArr, reversed):
        while low != high:
            mid = low + (high-low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1
                else:
                    high = mid 
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid
        return low