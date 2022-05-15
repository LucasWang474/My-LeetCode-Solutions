/**
 * https://leetcode.com/problems/permutations/
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    if (nums.length <= 1) {
        return [nums.slice()];
    }

    const results = [];

    for (let i = 0; i < nums.length; i++) {
        const head = nums[i];
        const newNums = nums.slice(0, i).concat(nums.slice(i + 1, nums.length));
        const cur = permute(newNums);
        cur.map(ele => ele.unshift(head));
        results.push(...cur);
    }
    return results;
};
