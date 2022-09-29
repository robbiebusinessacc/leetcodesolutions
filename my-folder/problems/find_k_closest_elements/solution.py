class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left=0;right=len(arr)-k
        while left<right:
            middle=left+(right-left)//2
            if x-arr[middle]>arr[middle+k]-x:left=middle+1
            else:right=middle
        return arr[left:left+k]