/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    let prefix = [1];
    for (let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i - 1] * nums[i - 1];
    }

    let postfix = 1;
    let res = prefix;
    for (let i = res.length - 1; i >= 0; i--) {
        res[i] = prefix[i] * postfix;
        postfix *= nums[i];
    }
    return res;
};
