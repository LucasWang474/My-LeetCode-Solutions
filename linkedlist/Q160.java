/**
 * https://leetcode.com/problems/intersection-of-two-linked-lists/
 */
public class Q160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode ptrA = headA, ptrB = headB;
        while (ptrA != ptrB) {
            ptrA = (ptrA != null) ? ptrA.next : headB;
            ptrB = (ptrB != null) ? ptrB.next : headA;
        }
        return ptrA;
    }
}
