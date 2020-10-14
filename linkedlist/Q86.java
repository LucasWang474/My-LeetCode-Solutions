public class Q86 {
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(), lessPtr = less;
        ListNode other = new ListNode(), otherPtr = other;
        while (head != null) {
            if (head.val < x) {
                lessPtr.next = head;
                lessPtr = lessPtr.next;
            } else {
                otherPtr.next = head;
                otherPtr = otherPtr.next;
            }
            head = head.next;
        }
        lessPtr.next = other.next;
        otherPtr.next = null;
        return less.next;
    }
}
