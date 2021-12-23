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
    if (!head || !head.next) return true;

    // Find the middle, left leaned
    let dummy = new ListNode(0, head);
    let slow = dummy, fast = dummy;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the right part
    let mid = slow;
    let right = mid.next;
    mid.next = null;
    // Reverse
    let reversedRight = null;
    while (right) {
        let next = right.next;
        right.next = reversedRight;
        reversedRight = right;
        right = next;
    }

    // Compare
    let ptr1 = head, ptr2 = reversedRight;
    while (ptr1 && ptr2) {
        if (ptr1.val !== ptr2.val) return false;
        ptr1 = ptr1.next;
        ptr2 = ptr2.next;
    }

    // Optional: restore the list
    // Reverse right again
    let originalRight = null;
    while (reversedRight) {
        let next = reversedRight.next;
        reversedRight.next = originalRight;
        originalRight = reversedRight;
        reversedRight = next;
    }
    mid.next = originalRight;

    return true;
};


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
