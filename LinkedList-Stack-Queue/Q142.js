/**
 * Definition for singly-linked list.
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}


/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
    // Check if there is a cycle
    let slow = head, fast = head;
    while (fast && fast.next) {
        [slow, fast] = [slow.next, fast.next.next];
        if (slow === fast) break;
    }
    if (!fast || !fast.next) return null;

    // Find the joint
    let ptr1 = head, ptr2 = slow;
    while (ptr1 !== ptr2) {
        [ptr1, ptr2] = [ptr1.next, ptr2.next];
    }
    return ptr1;
};
