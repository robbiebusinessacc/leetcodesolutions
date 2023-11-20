class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        z=sum(travel)*3
        garbage_len=len(garbage)
        for trash in garbage:
            for i in "MPG":z+=trash.count(i)
        for i in "MPG":
            x=1
            while i not in garbage[garbage_len-x] and x!=garbage_len:
                z-=travel[::-1][x-1]
                x+=1
        return z