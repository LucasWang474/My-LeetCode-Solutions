// https://leetcode.com/problems/fibonacci-number/
/**
 * Iterative, best, O(n) time, O(1) space
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    if (n <= 1) {
        return n;
    }

    // 0, 1, 1, 2, 3, 5, 8, 13, ...
    let a = 0, b = 1;
    while (n > 1) {
        [a, b] = [b, a + b];
        n--;
    }
    return b;
};


/**
 * Recursive
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
};


/**
 * DP, bottom up
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    if (n <= 1) {
        return n;
    }

    const dp = [0, 1];
    while (n > 1) {
        const LEN = dp.length;
        dp.push(dp[LEN - 1] + dp[LEN - 2]);
        n--;
    }

    return dp[dp.length - 1];
};


/**
 * DP,top down
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    const dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;

    function helper(cur) {
        if (dp[cur] === undefined) {
            dp[cur] = helper(cur - 1) + helper(cur - 2);
        }
        return dp[cur];
    }

    return helper(n);
};
