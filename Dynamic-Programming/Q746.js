// https://leetcode.com/problems/min-cost-climbing-stairs/
/**
 * Recursive, bottom up with memorization
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
    const LEN = cost.length;
    const dp = new Array(cost.length);

    function helper(i) {
        if (i >= LEN) {
            return 0;
        }

        if (dp[i] === undefined) {
            dp[i] = cost[i] + Math.min(helper(i + 1), helper(i + 2));
        }
        return dp[i];
    }

    return Math.min(helper(0), helper(1));
};


// Iterative, top down with memorization
var minCostClimbingStairs = function (cost) {
    const LEN = cost.length;
    const dp = (new Array(cost.length + 2)).fill(0);

    // dp[i] = cost[i] + Math.min(dp[i + 1], dp[i + 2])

    for (let i = LEN - 1; i >= 0; i--) {
        dp[i] = cost[i] + Math.min(dp[i + 1], dp[i + 2]);
    }
    return Math.min(dp[0], dp[1]);
};


// Iterative, top down with two variables
var minCostClimbingStairs = function (cost) {
    const LEN = cost.length;

    let prev = 0, prevPrev = 0, cur = 0;
    for (let i = LEN - 1; i >= 0; i--) {
        cur = cost[i] + Math.min(prev, prevPrev);
        [prev, prevPrev] = [cur, prev];
    }
    return Math.min(prev, prevPrev);
};
