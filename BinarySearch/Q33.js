/**
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let L = 0, R = nums.length - 1;
    while (L <= R) {
        let mid = L + ((R - L) >> 1);
        if (nums[mid] === target) return mid;

        if (nums[L] <= nums[mid]) {
            // Mid is in the left sorted array

            if (target > nums[mid] || target < nums[L]) {
                L = mid + 1;
            } else {
                R = mid - 1;
            }
        } else {
            // Mid is in the right sorted array
            if (target < nums[mid] || target > nums[R]) {
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }
    }
    return -1;
};
