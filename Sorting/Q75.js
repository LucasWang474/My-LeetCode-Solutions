/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {

};


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