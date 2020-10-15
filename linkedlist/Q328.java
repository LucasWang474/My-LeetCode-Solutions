/**
 * https://leetcode.com/problems/odd-even-linked-list/
 */
public class Q328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;

        ListNode evenHead = head.next;
        ListNode oddPtr = head, evenPtr = evenHead;

        while (evenPtr != null && evenPtr.next != null) {
            oddPtr.next = evenPtr.next;
            oddPtr = oddPtr.next;
            evenPtr.next = oddPtr.next;
            evenPtr = evenPtr.next;
        }
        oddPtr.next = evenHead;
        return head;
    }
}
