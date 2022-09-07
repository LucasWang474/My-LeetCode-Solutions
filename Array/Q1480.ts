// https://leetcode.com/problems/running-sum-of-1d-array/
function runningSum(nums: number[]): number[] {
  let prevSum = 0;
  const res = [];

  for (let num of nums) {
    prevSum += num;
    res.push(prevSum);
  }

  return res;
}
