class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min_idx = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
            else:
                diff = max(diff, prices[i] - prices[min_idx])
        
        return diff
        