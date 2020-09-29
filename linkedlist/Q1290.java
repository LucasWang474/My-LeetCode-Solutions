/**
 * https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 */
public class Q1290 {
    public int getDecimalValue(ListNode head) {
        int result = 0;
        for(ListNode ptr = head; ptr != null; ptr = ptr.next) {
            result <<= 1;
            result += ptr.val;
        }
        return result;
    }
}
