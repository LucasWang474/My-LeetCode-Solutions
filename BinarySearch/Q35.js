/**
 * https://leetcode.com/problems/search-insert-position/
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let L = 0, R = nums.length - 1;
    while (L <= R) {
        let mid = L + ((R - L) >> 1);
        if (nums[mid] === target) return mid;
        if (nums[mid] < target) L = mid + 1;
        else R = mid - 1;
    }
    return L;
};
