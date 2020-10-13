public class Q61 {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        ListNode ptr = head;
        int length = 1;
        while (ptr.next != null) {
            ptr = ptr.next;
            length++;
        }
        ListNode tail = ptr;

        if (k % length == 0) return head;

        int count = length - k % length - 1;
        ptr = head;
        while (count-- > 0) {
            ptr = ptr.next;
        }
        ListNode newHead = ptr.next;
        ptr.next = null;
        tail.next = head;
        return newHead;
    }
}
