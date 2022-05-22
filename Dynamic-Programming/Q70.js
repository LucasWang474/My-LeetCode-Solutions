// https://leetcode.com/problems/climbing-stairs/
/**
 * Time O(n), space O(1)
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    // 逆向思维，在达到 n 步之前有两种情况：n - 1 和 n - 2
    // 所以 T(n) = T(n - 1) + T(n - 2)
    // 1: 1
    // 2: 2
    // 3: 2 + 1 = 3
    // 4: 3 + 2 = 5
    // 5: 5 + 3 = 8

    if (n < 4) {
        return n;
    }

    let a = 3, b = 5;
    while (n > 4) {
        [a, b] = [b, a + b];
        n--;
    }
    return b;
};
