// https://leetcode.com/problems/n-th-tribonacci-number/
/**
 * Iterative, O(n) time, O(1) space
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
    if (n < 2) {
        return n;
    }

    let a = 0, b = 1, c = 1;
    while (n > 2) {
        [a, b, c] = [b, c, a + b + c];
        n--;
    }
    return c;
};
