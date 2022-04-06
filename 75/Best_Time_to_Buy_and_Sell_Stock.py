'''Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''

def maxProfit(prices):
        l,r = 0,1
        maxDiff = 0

        while r < len(prices):
            if prices[l] <  prices[r]:
                profit = prices[r]-prices[l]
                maxDiff = max(maxDiff,profit)
            else:
                l = r
            r += 1

        return maxDiff
