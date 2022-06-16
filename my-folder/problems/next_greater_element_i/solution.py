class Solution:
    def nextGreaterElement(self, nums1,nums2):
        ans=[]
        stack=[]
        mapng={}
        for n in nums2:
            while stack and n>stack[-1]:
                mapng[stack.pop()]=n
            stack.append(n)
        while stack:
            mapng[stack.pop()]=-1  
        for n in nums1:
            ans.append(mapng[n])
        return ans

        