/**
 * https://leetcode.com/problems/reverse-linked-list/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    // Recursive
    if (!head || !head.next) {
        return head;
    }
    const newTail = head.next;
    const newHead = reverseList(head.next);
    newTail.next = head;
    head.next = null;
    return newHead;
};

var reverseList = function (head) {
    // Iterative
    let reversed = null, temp;
    while (head) {
        temp = head.next;
        head.next = reversed;
        reversed = head;
        head = temp;
    }
    return reversed;
};
