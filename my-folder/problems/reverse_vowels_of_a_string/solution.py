class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=''
        for i in s:
            if i.lower() in 'aeiou':
                vowels+=i
        z=''
        j=len(vowels)-1
        a=0
        for i in s:
            a+=1
            if i.lower() in'aeiou':
                z+=vowels[j]
                j-=1
            else:
                z+=i
        return z