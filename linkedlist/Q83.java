/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list/
 */
public class Q83 {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode dummy = new ListNode(head.val - 1, head), ptr = dummy;
        int prev = dummy.val;
        while (ptr.next != null) {
            if (ptr.next.val == prev) {
                ptr.next = ptr.next.next;
            } else {
                prev = ptr.next.val;
                ptr = ptr.next;
            }
        }

        return dummy.next;
    }
}
