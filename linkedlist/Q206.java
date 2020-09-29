/**
 * https://leetcode.com/problems/reverse-linked-list/
 */
public class Q206 {
    // recursive
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode reversed = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return reversed;
    }

    // iterative
    public ListNode reverseList2(ListNode head) {
        ListNode reversed = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = reversed;
            reversed = head;
            head = temp;
        }
        return reversed;
    }
}
