function searchRange(nums: number[], target: number): number[] {
  let L = 0, R = nums.length - 1, M, cur;
  let res1 = -1;
  while (L <= R) {
    M = Math.floor((L + R) / 2);
    cur = nums[M];

    if (cur < target) {
      L = M + 1;
    } else if (cur > target) {
      R = M - 1;
    } else {
      res1 = M;
      R = M - 1;
    }
  }

  L = 0;
  R = nums.length - 1;
  let res2 = -1;
  while (L <= R) {
    M = Math.floor((L + R) / 2);
    cur = nums[M];

    if (cur < target) {
      L = M + 1;
    } else if (cur > target) {
      R = M - 1;
    } else {
      res2 = M;
      L = M + 1;
    }
  }

  return [res1, res2];
}
