public class Q707 {
    /**
     * Your MyLinkedList object will be instantiated and called as such:
     * MyLinkedList obj = new MyLinkedList();
     * int param_1 = obj.get(index);
     * obj.addAtHead(val);
     * obj.addAtTail(val);
     * obj.addAtIndex(index,val);
     * obj.deleteAtIndex(index);
     */
    public static class MyLinkedList {
        private static class Node {
            Node prev;
            int val;
            Node next;

            Node(Node prev, int val, Node next) {
                this.prev = prev;
                this.val = val;
                this.next = next;
            }

            Node() {
            }
        }

        private final Node sentinel;
        private int size;

        /** Initialize your data structure here. */
        public MyLinkedList() {
            sentinel = new Node();
            sentinel.prev = sentinel;
            sentinel.next = sentinel;
        }

        private boolean isEmpty() {
            return size <= 0;
        }

        /** Get the value of the index-th node in the linked list.
         * If the index is invalid, return -1. */
        public int get(int index) {
            if (isEmpty() || index < 0 || index >= size) return -1;

            Node ptr = sentinel;
            while (index-- > 0) {
                ptr = ptr.next;
            }
            return ptr.next.val;
        }

        /** Add a node of value val before the first element of the linked list.
         * After the insertion, the new node will be the first node of the linked list. */
        public void addAtHead(int val) {
            addAtIndex(0, val);
        }

        /** Append a node of value val to the last element of the linked list. */
        public void addAtTail(int val) {
            size++;
            Node newTail = new Node(sentinel.prev, val, sentinel);
            sentinel.prev = newTail;
            newTail.prev.next = newTail;
        }

        /** Add a node of value val before the index-th node in the linked list.
         * If index equals to the length of linked list,
         * the node will be appended to the end of linked list.
         * If index is greater than the length, the node will not be inserted. */
        public void addAtIndex(int index, int val) {
            if (index < 0 || index > size) return;

            if (index == size) {
                addAtTail(val);
                return;
            }

            Node prev = sentinel;
            while (index-- > 0) {
                prev = prev.next;
            }

            size++;
            Node newNode = new Node(prev, val, prev.next);
            prev.next = newNode;
            newNode.next.prev = newNode;
        }

        private void deleteTail() {
            if (isEmpty()) return;

            size--;
            Node tailPrev = sentinel.prev.prev;
            tailPrev.next = sentinel;
            sentinel.prev = tailPrev;
        }

        /** Delete the index-th node in the linked list, if the index is valid. */
        public void deleteAtIndex(int index) {
            if (isEmpty()) return;
            if (index < 0 || index >= size) return;
            if (index == size - 1) {
                deleteTail();
                return;
            }

            Node ptr = sentinel;
            while (index-- > 0) {
                ptr = ptr.next;
            }

            size--;
            Node newNext = ptr.next.next;
            newNext.prev = ptr;
            ptr.next = newNext;
        }

        public void print() {
            Node ptr = sentinel.next;
            while (ptr != sentinel) {
                System.out.print(ptr.val + "->");
                ptr = ptr.next;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        MyLinkedList myLinkedList = new MyLinkedList();

        myLinkedList.addAtHead(4);
        myLinkedList.print();

        myLinkedList.addAtHead(1);
        myLinkedList.print();

        myLinkedList.addAtHead(5);
        myLinkedList.print();

        myLinkedList.deleteAtIndex(3);
        myLinkedList.print();

        myLinkedList.addAtHead(7);
        myLinkedList.print();

        myLinkedList.addAtHead(1);
        myLinkedList.print();

        System.out.println(myLinkedList.get(3));
        System.out.println(myLinkedList.get(3));
        System.out.println(myLinkedList.get(3));
    }
}
