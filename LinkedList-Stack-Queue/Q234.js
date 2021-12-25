/**
 * https://leetcode.com/problems/palindrome-linked-list/
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}


/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
    // Get the middle node, left leaned
    const dummy = new ListNode(0, head);
    let slow = dummy, fast = dummy;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Get right and truncate
    const mid = slow;
    const reversedRight = reverseList(mid.next);
    mid.next = null;

    // Compare one by one
    let isPalindrome = true;
    let ptr1 = head, ptr2 = reversedRight;
    while (ptr1 && ptr2) {
        if (ptr1.val !== ptr2.val) {
            isPalindrome = false;
            break;
        }
        ptr1 = ptr1.next;
        ptr2 = ptr2.next;
    }

    // Restore the right
    mid.next = reverseList(reversedRight);

    return isPalindrome;
};


function reverseList(head) {
    // Reverse right
    let reversed = null;
    while (head) {
        let next = head.next;
        head.next = reversed;
        reversed = head;
        head = next;
    }
    return reversed;
}


/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome2 = function (head) {
    let stack = [];

    let ptr = head;
    while (ptr) {
        stack.push(ptr.val);
        ptr = ptr.next;
    }

    while (head) {
        if (head.val !== stack.pop()) return false;
        head = head.next;
    }
    return true;
};
