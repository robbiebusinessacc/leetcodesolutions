class Solution:
    def canMakeArithmeticProgression(self,arr):
        return arr.sort()or all([j-i==arr[1]-arr[0]for(i,j)in zip(arr,arr[1:])])