# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices):
        stack = []
        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
