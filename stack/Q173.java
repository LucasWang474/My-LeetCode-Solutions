import java.util.Deque;
import java.util.LinkedList;

public class Q173 {
    private static class BSTIterator {
        private final Deque<TreeNode> deque = new LinkedList<>();

        public BSTIterator(TreeNode root) {
            push(root);
        }

        private void push(TreeNode root) {
            while (root != null) {
                deque.addLast(root);
                root = root.left;
            }
        }

        /** @return the next smallest number */
        public int next() {
            TreeNode current = deque.removeLast();
            int result = current.val;
            push(current.right);
            return result;
        }

        /** @return whether we have a next smallest number */
        public boolean hasNext() {
            return !deque.isEmpty();
        }
    }

    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}
