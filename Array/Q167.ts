function twoSum(numbers: number[], target: number): number[] {
  let L = 0, R = numbers.length - 1;
  while (L < R) {
    const cur = numbers[L] + numbers[R];
    if (cur < target) {
      L += 1;
    } else if (cur > target) {
      R -= 1;
    } else {
      return [L + 1, R + 1];
    }
  }
  return [-1, -1];
}


// Test cases

// Case 1: Input: numbers = [2,3,4], target = 6
// Output: [1, 3]
console.log('Expected: [1, 3]');
console.log('Actual: ', twoSum([2, 3, 4], 6));

// Case 2: Input: numbers = [2,3,4], target = 7
// Output: [2, 3]
console.log('Expected: [2, 3]');
console.log('Actual: ', twoSum([2, 3, 4], 7));

// Case 3: Input: numbers = Input: numbers = [2,7,11,15], target = 9
// Output: [1, 2]
console.log('Expected: [1, 2]');
console.log('Actual: ', twoSum([2, 7, 11, 15], 9));

// Case 4: Input: numbers = [3,2,4], target = 6
// Output: [2, 3]
console.log('Expected: [2, 3]');
console.log('Actual: ', twoSum([3, 2, 4], 6));


// Case 5: Input: numbers = [1,2,3,4,4,9,56,90], target = 8
// Output: [4, 5]
