class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies);return(True if candy+extraCandies>=greatest else False for candy in candies)