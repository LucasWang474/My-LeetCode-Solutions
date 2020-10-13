public class Q25 {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head), ptr = dummy;
        while (ptr.next != null) {
            int count = 1;
            ListNode tail = ptr.next;
            while (tail != null && count++ < k) {
                tail = tail.next;
            }
            if (tail == null) break;

            ListNode oldHead = ptr.next, newHead = tail.next;
            tail.next = null;
            ListNode reversed = reverseList(oldHead);
            oldHead.next = newHead;
            ptr.next = reversed;
            ptr = oldHead;
        }
        return dummy.next;
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
