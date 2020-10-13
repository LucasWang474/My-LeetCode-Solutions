import java.util.Comparator;
import java.util.PriorityQueue;

public class Q23 {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        // modify lists
        int interval = 1;
        while (interval < lists.length) {
            for (int i = 0; i < lists.length - interval; i += interval * 2) {
                lists[i] = merge(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }
        return lists[0];
    }

    // does not modify lists
    private ListNode mergeKLists(ListNode[] lists, int lo, int hi) {
        if (lo > hi) return null;
        if (lo == hi) return lists[lo];

        int mid = lo + (hi - lo) / 2;
        ListNode left = mergeKLists(lists, lo, mid);
        ListNode right = mergeKLists(lists, mid + 1, hi);
        return merge(left, right);
    }

    public ListNode mergeKLists2(ListNode[] lists) {
        if (lists == null) return null;

        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(listNode -> listNode.val));
        for (ListNode listNode : lists) {
            if (listNode != null) pq.add(listNode);
        }

        ListNode dummy = new ListNode(), ptr = dummy;
        while (!pq.isEmpty()) {
            ListNode min = pq.remove();
            ptr.next = min;
            ptr = ptr.next;

            if (min.next != null) {
                pq.add(min.next);
            }
        }
        return dummy.next;
    }

    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), ptr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                ptr.next = l1;
                l1 = l1.next;
            } else {
                ptr.next = l2;
                l2 = l2.next;
            }
            ptr = ptr.next;
        }
        ptr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
