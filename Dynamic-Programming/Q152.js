/**
 * https://leetcode.com/problems/maximum-product-subarray/
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    let curMax = 1, curMin = 1;
    let res = nums[0];

    for (let num of nums) {
        let temp = curMax * num;
        curMax = Math.max(temp, curMin * num, num);
        curMin = Math.min(temp, curMin * num, num);
        res = Math.max(curMax, res);
    }

    return res;
};
