/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
    // Count sort
    let maxNum = Math.max(...nums), minNum = Math.min(...nums);
    let counts = new Array(maxNum - minNum + 1).fill(0);
    for (let num of nums) counts[num - minNum]++;

    let sum = 0, i = 0, N = nums.length, isLeft = true;
    while (i < counts.length && N > 0) {
        if (counts[i]) {
            if (isLeft) {
                sum += Q234
                i + minNum;
                isLeft = false;
            } else {
                isLeft = true;
            }
            counts[i]--;
            N--;
        } else {
            i++;
        }
    }
    return sum;
};
