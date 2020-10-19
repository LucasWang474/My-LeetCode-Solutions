import java.util.Deque;
import java.util.LinkedList;

public class Q933 {
    /**
     * Your RecentCounter object will be instantiated and called as such:
     * RecentCounter obj = new RecentCounter();
     * int param_1 = obj.ping(t);
     */
    private static class RecentCounter {
        private final Deque<Integer> deque = new LinkedList<>();

        public RecentCounter() {

        }

        public int ping(int t) {
            deque.addLast(t);
            while (!deque.isEmpty() && deque.getFirst() < t - 3000) {
                deque.removeFirst();
            }
            return deque.size();
        }
    }
}
