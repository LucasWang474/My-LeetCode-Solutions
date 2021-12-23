/**
 * https://leetcode.com/problems/maximum-subarray/
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let maxSum = nums[0], curSum = 0;
    for (let i = 0; i < nums.length; i++) {
        curSum += nums[i];
        maxSum = Math.max(maxSum, curSum);
        if (curSum < 0) curSum = 0;
    }
    return maxSum;
};
