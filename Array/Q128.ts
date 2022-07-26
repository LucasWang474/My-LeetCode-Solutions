function longestConsecutive(nums: number[]): number {
  const set = new Set(nums);

  let maxLen = 0, curLen, left, right;

  for (let num of nums) {
    if (set.has(num)) {
      curLen = 1;

      right = num + 1;
      while (set.has(right)) {
        set.delete(right);
        curLen += 1;
        right += 1;
      }

      left = num - 1;
      while (set.has(left)) {
        set.delete(left);
        curLen += 1;
        left -= 1;
      }

      maxLen = Math.max(maxLen, curLen);
    }
  }

  return maxLen;
}


// Test cases
// Case 1
console.log('Expected: 4, Actual: ' + longestConsecutive([100, 4, 200, 1, 3, 2]));
console.log(4 === longestConsecutive([100, 4, 200, 1, 3, 2]));
// Case 2
console.log('Expected: 4, Actual: ' + longestConsecutive([-2, -1, -3, -4]));
console.log(4 === longestConsecutive([-2, -1, -3, -4]));
// Case 3
console.log('Expected: 0, Actual: ' + longestConsecutive([]));
console.log(0 === longestConsecutive([]));
// Case 4
console.log('Expected: 1, Actual: ' + longestConsecutive([1]));
console.log(1 === longestConsecutive([1]));
// Case 5
console.log('Expected: 9, Actual: ' + longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
console.log(9 === longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
