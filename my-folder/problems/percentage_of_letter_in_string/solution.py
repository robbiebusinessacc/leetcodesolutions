class Solution:
    def percentageLetter(self,s,letter):
        return s.count(letter)*100//len(s)