import java.util.Deque;
import java.util.LinkedList;

public class Q445 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Deque<Integer> deque1 = new LinkedList<>(), deque2 = new LinkedList<>();
        while (l1 != null) {
            deque1.addLast(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            deque2.addLast(l2.val);
            l2 = l2.next;
        }

        ListNode result = null;
        int carry = 0, sum;
        while (!deque1.isEmpty() || !deque2.isEmpty() || carry > 0) {
            sum = carry;
            if (!deque1.isEmpty()) {
                sum += deque1.removeLast();
            }
            if (!deque2.isEmpty()) {
                sum += deque2.removeLast();
            }
            carry = sum / 10;
            result = new ListNode(sum % 10, result);
        }
        return result;
    }
}
