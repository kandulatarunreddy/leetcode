from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Keep track of the minimum price so far
        At each day, imagine selling today and update max profit
	    '''
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]

    print("Input:", prices)
    print("Max Profit:", solution.maxProfit(prices))