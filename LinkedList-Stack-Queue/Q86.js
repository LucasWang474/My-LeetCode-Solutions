/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
  let LT = new ListNode(), ptrLT = LT;
  let GTE = new ListNode(), ptrGTE = GTE;
  
  while (head) {
    if (head.val < x) {
      ptrLT.next = new ListNode(head.val);
      ptrLT = ptrLT.next;
    } else {
      ptrGTE.next = new ListNode(head.val);
      ptrGTE = ptrGTE.next;
    }
    head = head.next;
  }
  
  ptrLT.next = GTE.next;
  return LT.next;
};
