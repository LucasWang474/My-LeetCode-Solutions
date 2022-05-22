// https://leetcode.com/problems/house-robber-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    function helper(nums) {
        let [a, b, c] = [0, 0, 0];
        let i = nums.length - 1, cur;
        while (i >= 0) {
            cur = nums[i] + Math.max(b, c);
            [a, b, c] = [cur, a, b];
            i--;
        }
        return Math.max(a, b);
    }

    const unheaded = nums.slice(1);
    const untailed = nums.slice(0, nums.length - 1);
    return Math.max(nums[0], helper(unheaded), helper(untailed));
};
