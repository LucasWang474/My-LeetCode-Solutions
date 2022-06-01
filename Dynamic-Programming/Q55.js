// https://leetcode.com/problems/jump-game/

/**
 * Recursive, bottom up with memorization
 * Time O(n2), space O(n)
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
    if (nums.length < 2) {
        return true;
    }

    // dp[i] = dp[i + 1] || dp[i + 2] || ... || dp[i + nums[i]]

    const LEN = nums.length;
    const dp = new Array(LEN);

    function helper(i) {
        if (i >= (LEN - 1)) {
            return true;
        }

        if (dp[i] !== undefined) {
            return dp[i];
        }

        dp[i] = false;

        if (nums[i] > 0) {
            for (let j = i + nums[i]; (j > i) && !dp[i]; j--) {
                dp[i] ||= helper(j);
            }
        }

        return dp[i];
    }

    return helper(0);
};


// Top down
var canJump = function (nums) {
    if (nums.length < 2) {
        return true;
    }

    // dp[i] = dp[i + 1] || dp[i + 2] || ... || dp[i + nums[i]]

    const LEN = nums.length;
    const dp = new Array(LEN);

    function helper(i) {
        if (i >= (LEN - 1)) {
            return true;
        }

        if (dp[i] !== undefined) {
            return dp[i];
        }

        dp[i] = false;

        if (nums[i] > 0) {
            for (let j = i + nums[i]; (j > i) && !dp[i]; j--) {
                dp[i] ||= helper(j);
            }
        }

        return dp[i];
    }

    return helper(0);
};
