/**
 * https://leetcode.com/problems/linked-list-cycle/
 */
public class Q141 {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) break;
        }
        return fast != null && fast.next != null;
    }
}
141. Linked List Cycle141. Linked List Cycle