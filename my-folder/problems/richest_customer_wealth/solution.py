class Solution:
    def maximumWealth(self, accounts: List[List[int]]):
        return max([sum(account)for account in accounts])
        