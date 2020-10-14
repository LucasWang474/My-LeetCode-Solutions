import java.util.HashMap;
import java.util.Map;

public class Q138 {
    public Node copyRandomList1(Node head) {
        if (head == null) return null;

        Node ptr = head, next;

        while (ptr != null) {
            next = ptr.next;
            ptr.next = new Node(ptr.val);
            ptr.next.next = next;
            ptr = next;
        }

        ptr = head;
        while (ptr != null) {
            next = ptr.next.next;
            if (ptr.random != null) {
                ptr.next.random = ptr.random.next;
            }
            ptr = next;
        }

        ptr = head;
        Node dummy = new Node(0), cur = dummy;
        while (ptr != null) {
            cur.next = ptr.next;
            cur = cur.next;
            ptr.next = ptr.next.next;
            ptr = ptr.next;
        }
        return dummy.next;
    }

    public Node copyRandomList2(Node head) {
        if (head == null) return null;

        Map<Node, Node> oldToNew = new HashMap<>();

        for (Node ptr = head; ptr != null; ptr = ptr.next) {
            oldToNew.put(ptr, new Node(ptr.val));
        }

        for (Node ptr = head; ptr != null; ptr = ptr.next) {
            oldToNew.get(ptr).next = oldToNew.get(ptr.next);
            oldToNew.get(ptr).random = oldToNew.get(ptr.random);
        }
        return oldToNew.get(head);
    }
}


class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}