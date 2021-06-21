// https://leetcode.com/problems/merge-sorted-array/
public class Q88 {
    /**
     * Time: O(N)
     * Space: O(1)
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1;
        for (int k = m + n - 1; k >= 0; k--) {
            if      (i < 0)                 nums1[k] = nums2[j--];
            else if (j < 0)                 nums1[k] = nums1[i--];
            else if (nums1[i] > nums2[j])   nums1[k] = nums1[i--];
            else                            nums1[k] = nums2[j--];
        }
    }

    /**
     * Time: O(N)
     * Space: O(N)
     */
//    public void merge(int[] nums1, int m, int[] nums2, int n) {
//        int[] aux = new int[m + n];
//        for (int i = 0; i < m + n; i++) {
//            if (i < m)  {
//                aux[i] = nums1[i];
//            } else {
//                aux[i] = nums2[i - m];
//            }
//        }
//
//        int i = 0, j = m;
//        for (int k = 0; k < m + n; k++) {
//            if      (i >= m)            nums1[k] = aux[j++];
//            else if (j >= m + n)        nums1[k] = aux[i++];
//            else if (aux[i] < aux[j])   nums1[k] = aux[i++];
//            else                        nums1[k] = aux[j++];
//        }
//    }
}
