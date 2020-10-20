public class Q209 {
    public int minSubArrayLen(int goal, int[] nums) {
        int minLen = nums.length + 1, sum = 0, left = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            while (sum >= goal) {
                minLen = Math.min(minLen, i - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen % (nums.length + 1);
    }
}
