/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let prevMin = prices[0], maxProfit = 0;
    for (let i = 1; i < prices.length; i++) {
        maxProfit = Math.max(prices[i] - prevMin, maxProfit);
        prevMin = Math.min(prices[i], prevMin);
    }
    return maxProfit;
};
