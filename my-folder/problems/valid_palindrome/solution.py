class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter=''
        for l in s:
            l=l.lower()
            if l in 'qwertyuiopasdfghjklzx12345qwertyuiopasdfghjklzxcvbnm67890cvbnm':
                letter+=l
        return letter==letter[::-1]
                
        