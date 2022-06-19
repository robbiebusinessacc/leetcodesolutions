class Solution:
    def longestPalindrome(self, s):
        st = set()
        for char in s:
            if char not in st:st.add(char)
            else:st.remove(char)
        return len(s)-max(0,len(st)-1)
        