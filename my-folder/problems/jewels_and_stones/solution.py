class Solution:
    def numJewelsInStones(self, jewels,stones):
        return sum(map(stones.count,jewels))  
        