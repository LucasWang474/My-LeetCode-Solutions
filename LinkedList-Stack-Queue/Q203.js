/**
 * https://leetcode.com/problems/remove-linked-list-elements/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function (head, val) {
    const dummy = new ListNode(0, head);
    let ptr = dummy;
    while (ptr.next) {
        if (ptr.next.val === val) {
            ptr.next = ptr.next.next;
        } else {
            ptr = ptr.next;
        }
    }
    return dummy.next;
};
