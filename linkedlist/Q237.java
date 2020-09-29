/**
 * https://leetcode.com/problems/delete-node-in-a-linked-list/
 */
public class Q237 {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
