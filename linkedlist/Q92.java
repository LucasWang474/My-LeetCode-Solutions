public class Q92 {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0, head), prev = dummy;
        for (int i = 1; i < m; i++) {
            prev = prev.next;
        }

        ListNode reversed = null, ptr = prev.next;
        for (int j = m; j <= n; j++) {
            ListNode temp = ptr.next;
            ptr.next = reversed;
            reversed = ptr;
            ptr = temp;
        }

        ListNode oldHead = prev.next;
        oldHead.next = ptr;
        prev.next = reversed;
        return dummy.next;
    }
}
