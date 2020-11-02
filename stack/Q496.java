import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class Q496 {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> deque = new LinkedList<>();
        Map<Integer, Integer> numToGreater = new HashMap<>();
        for (int num : nums2) {
            while (!deque.isEmpty() && deque.getLast() < num) {
                numToGreater.put(deque.removeLast(), num);
            }
            deque.addLast(num);
        }

        int[] result = new int[nums1.length];
        for (int j = 0; j < nums1.length; j++) {
            result[j] = numToGreater.getOrDefault(nums1[j], -1);
        }
        return result;
    }


}
