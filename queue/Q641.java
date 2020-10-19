public class Q641 {
    private static class MyCircularDeque {
        private final int[] values;
        private int size;
        private int front;
        private int end;

        /** Initialize your data structure here. Set the size of the deque to be k. */
        public MyCircularDeque(int k) {
            values = new int[k];
        }

        private boolean init(int value) {
            if (!isEmpty()) return false;

            front = 0;
            end = 0;
            values[0] = value;
            size = 1;
            return true;
        }

        /** Adds an item at the front of Deque. Return true if the operation is successful. */
        public boolean insertFront(int value) {
            if (isFull()) return false;
            if (isEmpty()) return init(value);

            int newFront = Math.floorMod(front - 1, values.length);
            values[newFront] = value;
            front = newFront;
            size++;
            return true;
        }

        /** Adds an item at the rear of Deque. Return true if the operation is successful. */
        public boolean insertLast(int value) {
            if (isFull()) return false;
            if (isEmpty()) return init(value);

            int newEnd = Math.floorMod(end + 1, values.length);
            values[newEnd] = value;
            end = newEnd;
            size++;
            return true;
        }

        /** Deletes an item from the front of Deque. Return true if the operation is successful. */
        public boolean deleteFront() {
            if (isEmpty()) return false;

            front = Math.floorMod(front + 1, values.length);
            size--;
            return true;
        }

        /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
        public boolean deleteLast() {
            if (isEmpty()) return false;

            end = Math.floorMod(end - 1, values.length);
            size--;
            return true;
        }

        /** Get the front item from the deque. */
        public int getFront() {
            if (isEmpty()) return -1;

            return values[front];
        }

        /** Get the last item from the deque. */
        public int getRear() {
            if (isEmpty()) return -1;

            return values[end];
        }

        /** Checks whether the circular deque is empty or not. */
        public boolean isEmpty() {
            return size == 0;
        }

        /** Checks whether the circular deque is full or not. */
        public boolean isFull() {
            return size == values.length;
        }
    }
}
