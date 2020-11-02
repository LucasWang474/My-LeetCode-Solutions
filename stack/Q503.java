import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class Q503 {
    public int[] nextGreaterElements(int[] nums) {
        Deque<Integer> deque = new LinkedList<>();
        int[] result = new int[nums.length];
        Arrays.fill(result, -1);
        for (int i = 0; i < nums.length * 2; i++) {
            int index = i % nums.length;
            int num = nums[index];
            while (!deque.isEmpty() && nums[deque.getLast()] < num) {
                result[deque.removeLast()] = num;
            }
            deque.addLast(index);
        }
        return result;
    }
}
