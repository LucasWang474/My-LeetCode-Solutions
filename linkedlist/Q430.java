public class Q430 {
    public Node flatten(Node head) {
        flattenAndGetLast(head);
        return head;
    }

    public Node flattenAndGetLast(Node head) {
        if (head == null) return null;

        Node next = head.next, nextTail = flattenAndGetLast(next);
        Node child = head.child, childTail = flattenAndGetLast(child);
        head.child = null;

        if (childTail != null) {
            head.next = child;
            child.prev = head;
            head = childTail;
        }

        if (nextTail != null) {
            head.next = next;
            next.prev = head;
            head = nextTail;
        }

        return head;
    }

    private static class Node {
        public int val;
        public Node prev;
        public Node next;
        public Node child;
    }
}


