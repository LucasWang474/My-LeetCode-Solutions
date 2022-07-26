function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b); // NLogN

  const res: number[][] = [];

  // Complexity: O(N^2)
  const N = nums.length;
  for (let i = 0; i < N; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let L = i + 1, R = N - 1;
    while (L < R) {
      const threeSum = nums[i] + nums[L] + nums[R];
      if (threeSum < 0) {
        L += 1;
      } else if (threeSum > 0) {
        R -= 1;
      } else {
        res.push([nums[i], nums[L], nums[R]]);

        L += 1;
        R -= 1;
        while (L < R && nums[L] === nums[L - 1]) L += 1;
        while (L < R && nums[R] === nums[R + 1]) R -= 1;
      }
    }
  }

  return res;
}


// Case 1: Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
console.log('Expected: [[-1,-1,2],[-1,0,1]]');
console.log('Actual: ', threeSum([-1, 0, 1, 2, -1, -4]));

// Case 2: Input: nums = [0,1,1]
// Output: []
console.log('Expected: []');
console.log('Actual: ', threeSum([0, 1, 1]));

// Case 3: Input: nums = [0,0,0]
// Output: [[0,0,0]]
console.log('Expected: [[0,0,0]]');
console.log('Actual: ', threeSum([0, 0, 0]));

// Case 4: Input: nums = [-2,0,1,1,2]
// Output: [[-2,0,2],[-2,1,1]]
console.log('Expected: [[-2,0,2],[-2,1,1]]');
console.log('Actual: ', threeSum([-2, 0, 1, 1, 2]));
