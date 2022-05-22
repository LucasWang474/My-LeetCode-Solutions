// https://leetcode.com/problems/house-robber/
/**
 * Recursive, bottom up with memorization
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    // dp[i] = nums[i] + Math.max(dp[i + 2], dp[i + 3])
    const LEN = nums.length;
    const dp = new Array(LEN);

    function helper(i) {
        if (i >= LEN) {
            return 0;
        }

        if (dp[i] !== undefined) {
            return dp[i];
        }

        dp[i] = nums[i] + Math.max(helper(i + 2), helper(i + 3));
        return dp[i];
    }

    return Math.max(helper(0), helper(1));
};


// Iterative, top down with memorization
// Time O(n), space O(n)
var rob = function (nums) {
    // dp[i] = nums[i] + Math.max(dp[i + 2], dp[i + 3])
    const LEN = nums.length;
    const dp = (new Array(LEN + 3)).fill(0);

    for (let i = LEN - 1; i >= 0; i--) {
        dp[i] = nums[i] + Math.max(dp[i + 2], dp[i + 3]);
    }

    return Math.max(dp[0], dp[1]);
};


// Iterative, top down
// Time O(n), space O(1)
var rob = function (nums) {
    // dp[i] = nums[i] + Math.max(dp[i + 2], dp[i + 3])

    let [a, b, c] = [0, 0, 0];
    let i = nums.length - 1, cur;
    while (i >= 0) {
        cur = nums[i] + Math.max(b, c);
        [a, b, c] = [cur, a, b];
        i--;
    }
    return Math.max(a, b);
};
