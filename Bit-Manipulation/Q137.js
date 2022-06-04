/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const bitCounts = Array(32).fill(0);
    for (let num of nums) {
        for (let i = 0; i <= 31; i++) {
            bitCounts[i] += (num >> i) & 1;
        }
    }
    
    // 假设一个数组中只有一个数出现了 M 次，其余的都出现了 N 次，并且 1 <= M < N
    const N = 3; // 更大的那个出现次数
    let res = 0;
    for (let i = 0; i <= 31; i++) {
        if ((bitCounts[i] % N) !== 0) {
            res |= (1 << i);
        }
    }
    return res;
};
