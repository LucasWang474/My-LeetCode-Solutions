/**
 * https://leetcode.com/problems/array-partition-i/
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
    // Counting Sort
    const minNum = Math.min(...nums), maxNum = Math.max(...nums);
    const counts = new Array(maxNum - minNum + 1).fill(0);
    for (let num of nums) counts[num - minNum]++;

    let sum = 0;
    let isLeft = true, i = 0;
    while (i < counts.length) {
        if (counts[i]) {
            if (isLeft) {
                sum += (i + minNum);
                isLeft = false;
            } else {
                isLeft = true;
            }
            counts[i]--;
        } else {
            i++;
        }
    }
    return sum;
};
