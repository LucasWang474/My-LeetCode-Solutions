// Definition for a Node.
// NOTE: DO NOT COPY THE FOLLOWING FUNCTION TO LEETCODE
// OR IT WILL FAIL FOR NO REASON!!!
function Node(val, next, random) {
    this.val = val;
    this.next = next;
    this.random = random;
}

/**
 * https://leetcode.com/problems/copy-list-with-random-pointer/
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
    if (!head) return null;

    let ptr;

    // Iteration 1: create new nodes
    ptr = head;
    while (ptr) {
        ptr.next = new Node(ptr.val, ptr.next);
        ptr = ptr.next.next;
    }

    // Iteration 2: assign randoms
    ptr = head;
    while (ptr) {
        if (ptr.random) ptr.next.random = ptr.random.next;
        ptr = ptr.next.next;
    }

    // Iteration 3: reconstruct
    let newHead = head.next;
    ptr = head;
    while (ptr) {
        let oldNext = ptr.next.next;
        let newNext = ptr.next;

        newNext.next = oldNext ? oldNext.next : null;
        ptr.next = oldNext;
        ptr = ptr.next;
    }

    return newHead;
};


/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList2 = function (head) {
    let oldToNew = new Map([[null, null]]);

    let ptr = head;
    while (ptr) {
        oldToNew.set(ptr, new Node(ptr.val));
        ptr = ptr.next;
    }

    ptr = head;
    while (ptr) {
        oldToNew.get(ptr).next = oldToNew.get(ptr.next);
        oldToNew.get(ptr).random = oldToNew.get(ptr.random);
        ptr = ptr.next;
    }
    return oldToNew.get(head);
};
