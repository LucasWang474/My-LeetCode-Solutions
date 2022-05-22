/**
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    if (!nums || nums.length < 2) return nums;

    quickSort(nums, 0, nums.length - 1);
    return nums;
};


function quickSort(arr, lo, hi) {
    if (lo >= hi) return;

    let pivot = arr[Math.floor(Math.random() * (hi - lo + 1)) + lo];
    let [lt, gt] = partition(arr, pivot, lo, hi);
    quickSort(arr, lo, lt);
    quickSort(arr, gt, hi);
}


function partition(arr, pivot, L, R) {
    if (L >= R) return;

    let lt = L - 1, gt = R + 1;
    let i = L;
    while (i < gt) {
        let cur = arr[i];
        if (cur < pivot) {
            lt++;
            [arr[lt], arr[i]] = [arr[i], arr[lt]];
            i++;
        } else if (cur > pivot) {
            gt--;
            [arr[gt], arr[i]] = [arr[i], arr[gt]];
        } else {
            i++;
        }
    }
    return [lt, gt];
}
