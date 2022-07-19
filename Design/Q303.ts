class NumArray {
  private readonly sums: any[];

  constructor(nums: number[]) {
    this.sums = [0];

    let prev = 0;
    for (let num of nums) {
      prev += num;
      this.sums.push(prev);
    }
  }

  sumRange(left: number, right: number): number {
    return this.sums[right + 1] - this.sums[left];
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
