public class Q82 {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        ListNode dummy = new ListNode(head.val - 1, head), ptr = dummy;
        int prevVal = dummy.val;
        while (ptr.next != null) {
            if (ptr.next.val == prevVal) {
                ptr.next = ptr.next.next;
            } else if (ptr.next.next != null && ptr.next.val == ptr.next.next.val) {
                prevVal = ptr.next.val;
                ptr.next = ptr.next.next.next;
            } else {
                prevVal = ptr.next.val;
                ptr = ptr.next;
            }
        }
        return dummy.next;
    }
}
