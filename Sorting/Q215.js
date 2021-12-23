/**
 * @param {number[]} nums
 * @param {number} K
 * @return {number}
 */
var findKthLargest = function (nums, K) {
    // Quick Select
    K = nums.length - K;
    partition(nums, K, 0, nums.length - 1);
    return nums[K];
};


function partition(arr, K, L, R) {
    if (L >= R) return;

    let pivot = arr[Math.floor(Math.random() * (R - L + 1)) + L];
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

    if (K <= lt) {
        partition(arr, K, L, lt);
    } else if (K >= gt) {
        partition(arr, K, gt, R);
    }
}
