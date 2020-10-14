public class Q143 {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode mid = slow;
        ListNode reversed = reverseList(mid.next);
        mid.next = null;

        ListNode ptr = head, next;
        while (reversed != null) {
            next = ptr.next;
            ptr.next = reversed;
            reversed = reversed.next;
            ptr.next.next = next;
            ptr = next;
        }
    }

    private ListNode reverseList(ListNode head) {
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
