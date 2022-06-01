// https://leetcode.com/problems/delete-and-earn/
/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function (nums) {
    const MAX_NUM = 10000;
    const count = (new Array(MAX_NUM + 1)).fill(0);
    for (let num of nums) {
        count[num] += 1;
    }

    // dp[i] = i * count[i] + Math.max(dp[i + 2], dp[i + 3])
    const dp = (new Array(MAX_NUM + 4)).fill(0);
    for (let i = MAX_NUM; i >= 0; i--) {
        dp[i] = i * count[i] + Math.max(dp[i + 2], dp[i + 3]);
    }

    return Math.max(dp[0], dp[1]);
};


var deleteAndEarn = function (nums) {
    function rob(nums) {
        // dp[i] = nums[i] + Math.max(dp[i + 2], dp[i + 3])

        let [a, b, c] = [0, 0, 0];
        let i = nums.length - 1, cur;
        while (i >= 0) {
            cur = nums[i] + Math.max(b, c);
            [a, b, c] = [cur, a, b];
            i--;
        }
        return Math.max(a, b);
    }


    const MAX_NUM = 10000;
    const count = (new Array(MAX_NUM + 1)).fill(0);
    for (let num of nums) {
        count[num] += num;
    }
    return rob(count);
};
