class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        low,high = 1,length-2
        while low != high:
            mid = low + (high - low) // 2
            if arr[mid] < arr[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low