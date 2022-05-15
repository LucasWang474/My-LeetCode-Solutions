/**
 * https://leetcode.com/problems/add-two-numbers
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    const dummy = new ListNode(0);
    let ptr = dummy;

    let carry = 0;
    while (l1 || l2 || carry > 0) {
        let current = carry;
        if (l1) {
            current += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            current += l2.val;
            l2 = l2.next;
        }
        ptr.next = new ListNode(current % 10);
        ptr = ptr.next;
        carry = Math.trunc(current / 10);
    }
    return dummy.next;
};
