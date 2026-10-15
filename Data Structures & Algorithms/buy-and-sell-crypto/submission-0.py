class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Integer Array -> Integer
        # In which case subtraction would be the max value where you choose two diff numbers. (which you may need sliding window)
        # Question: Is array in-line? Can i assume for i=0 is day1?
        # Constraints: buy_day != sell_day
        # Example: prices = [10, 1, 5, 6, 7, 1]
        # profit >= 0
        # As you can see from the example if I ll do brute force, time complexity O(n*logn), can we do better would be sliding window which would give us O(n).

        # profit = 0
        # left = 0
        # best = 0

        # for right in range(len(prices)):
        #     profit += prices[right]
        #     while profit <= 0:
        #         profit -= prices[left]
        #         left += 1
        #     size = right - left + 1
        #     best = max(best,size)
        # return best


# Second Try
        l, r = 0, 1 # left = buy, right = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r #because this is the lowest that you can get for profit.
            r+=1 #until it is out of bond from while loop
        return maxP










        
        