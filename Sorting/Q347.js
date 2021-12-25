/**
 * https://leetcode.com/problems/top-k-frequent-elements/
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let numToFreq = {};
    for (let num of nums) {
        numToFreq[num] = (num in numToFreq) ? (numToFreq[num] + 1) : 0;
    }

    let freqToNums = new Array(nums.length + 1);
    for (let i = 0; i < freqToNums.length; i++) freqToNums[i] = [];
    for (let num in numToFreq) freqToNums[numToFreq[num]].push(num);

    let res = [];
    let i = freqToNums.length - 1;
    while (i >= 0 && res.length < k) {
        if (freqToNums[i].length > 0) res.push(freqToNums[i].pop());
        else i--;
    }
    return res;
};
