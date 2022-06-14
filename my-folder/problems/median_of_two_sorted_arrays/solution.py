class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        lst=sorted(nums1+nums2)
        mid=int(len(lst)/2)-1
        if(len(lst)%2==0):return(lst[mid]+lst[mid+1])/2
        else:return lst[mid+1]
        