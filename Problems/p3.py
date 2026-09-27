"""
Problem 3
You are given an integer array prices where prices[i] represents the price of a stock on day i.
Choose one day to buy the stock and a later day to sell it.
Find the maximum profit you can achieve from this transaction.
If you cannot make a profit, return 0.
"""

def maxProfit(prices):

    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices:

        if price < minimum_price:
            minimum_price = price

        profit = price - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


prices = [5, 2, 6, 9, 3, 8, 2, 10]

print("Maximum Profit:", maxProfit(prices))