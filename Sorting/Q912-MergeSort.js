/**
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    if (!nums || nums.length < 2) return nums;

    mergeSort(nums, new Array(nums.length), 0, nums.length - 1);
    return nums;
};


function mergeSort(arr, aux, L, R) {
    if (L >= R) return;

    const mid = L + ((R - L) >> 1);
    mergeSort(arr, aux, L, mid);
    mergeSort(arr, aux, mid + 1, R);
    merge(arr, aux, L, mid, R);
}


function merge(arr, aux, L, mid, R) {
    if (L >= R) return;

    for (let i = L; i <= R; i++) aux[i] = arr[i];

    let leftI = L, rightI = mid + 1;
    for (let i = L; i <= R; i++) {
        if (rightI > R || leftI <= mid && aux[leftI] <= aux[rightI]) {
            arr[i] = aux[leftI];
            leftI++;
        } else {
            arr[i] = aux[rightI];
            rightI++;
        }
    }
}
