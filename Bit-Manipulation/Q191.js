/**
 * https://leetcode.com/problems/number-of-1-bits/
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
    let count = 0;
    while (n) {
        n ^= n & -n;
        count++;
    }
    return count;
};
