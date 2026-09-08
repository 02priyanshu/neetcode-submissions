class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        lowest=prices[0]
        for i in prices:
            if i<lowest:
                lowest=i
            if i-lowest>res:
                res=i-lowest
        return res