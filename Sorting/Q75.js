/**
 * https://leetcode.com/problems/sort-colors/
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
    let pivot = 1;
    let lt = -1, gt = nums.length;
    let i = 0;
    while (i < gt) {
        let cur = nums[i];
        if (cur < pivot) {
            lt++;
            [nums[lt], nums[i]] = [nums[i], nums[lt]];
            i++;
        } else if (cur > pivot) {
            gt--;
            [nums[gt], nums[i]] = [nums[i], nums[gt]];
        } else {
            i++;
        }
    }
};