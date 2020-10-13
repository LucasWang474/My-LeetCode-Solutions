public class Q24 {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head), ptr = dummy;
        while (ptr.next != null && ptr.next.next != null) {
            ListNode first = ptr.next, second = ptr.next.next;
            first.next = second.next;
            second.next = first;
            ptr.next = second;
            ptr = first;
        }
        return dummy.next;
    }

    public ListNode swapPairs2(ListNode oldHead) {
        if (oldHead == null || oldHead.next == null) return oldHead;

        ListNode newHead = oldHead.next;
        oldHead.next = swapPairs2(oldHead.next.next);
        newHead.next = oldHead;
        return newHead;
    }
}
