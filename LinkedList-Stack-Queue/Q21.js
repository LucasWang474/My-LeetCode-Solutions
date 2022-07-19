/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
  const dummy = new ListNode();
  
  let ptr = dummy;
  while (list1 && list2) {
    if (list1.val < list2.val) {
      ptr.next = new ListNode(list1.val);
      list1 = list1.next;
    } else {
      ptr.next = new ListNode(list2.val);
      list2 = list2.next;
    }
    ptr = ptr.next;
  }
  ptr.next = list1 ? list1 : list2;
  
  return dummy.next;
};
