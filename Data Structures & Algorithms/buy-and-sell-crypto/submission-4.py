class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy pointer (left of the window)
        right = 1  # Sell pointer (right of the window)
        max_profit = 0

        while right < len(prices):
            # Check if the current transaction is profitable
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # If prices[right] is lower than or equal to prices[left],
                # shift the left pointer to the right pointer's position
                left = right
            right += 1

        return max_profit