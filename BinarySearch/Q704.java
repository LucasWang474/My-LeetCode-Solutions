// https://leetcode.com/problems/binary-search/
public class Q704 {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int cmp = Integer.compare(target, nums[mid]);
            if (cmp < 0)      hi = mid - 1;
            else if (cmp > 0) lo = mid + 1;
            else              return mid;
        }
        return -1;
    }
}
