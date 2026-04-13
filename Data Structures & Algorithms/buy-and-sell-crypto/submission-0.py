class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p_max = 0

        while r < len(prices):
            temp_max = 0
            if prices[r] > prices[l]:
                temp_max = prices[r]-prices[l]
                p_max =max(temp_max,p_max)
            else:
                l = r
            r+=1
            
        return p_max




        