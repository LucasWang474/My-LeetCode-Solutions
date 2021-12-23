/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function (nums) {
    let xor = (a, b) => a ^ b;
    let aXORb = nums.reduce(xor);
    let rightMostOne = aXORb & -aXORb
    let aOrb = nums.filter(ele => (ele & rightMostOne) === 0).reduce(xor);
    return [aOrb, aXORb ^ aOrb];
};
