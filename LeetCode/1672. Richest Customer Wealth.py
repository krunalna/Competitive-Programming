#1672. Richest Customer Wealth

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxwealth = 0
        
        for account in accounts:
            maxwealth = max( maxwealth, sum(account))
            
        return maxwealth

        