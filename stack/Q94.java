import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class Q94 {
    // Threaded Binary Tree
    public List<Integer> inorderTraversal3(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        TreeNode current = root;
        while (current != null) {
            if (current.left == null) {
                result.add(current.val);
                current = current.right;
            } else {
                TreeNode left = current.left;

                TreeNode rightMost = left;
                while (rightMost.right != null) {
                    rightMost = rightMost.right;
                }

                current.left = null;
                rightMost.right = current;
                current = left;
            }
        }
        return result;
    }

    // Stack
    public List<Integer> inorderTraversal2(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> deque = new LinkedList<>();
        TreeNode current = root;
        while (current != null || !deque.isEmpty()) {
            while (current != null) {
                deque.addLast(current);
                current = current.left;
            }
            current = deque.removeLast();
            result.add(current.val);
            current = current.right;
        }
        return result;
    }

    // Recursion
    public List<Integer> inorderTraversal1(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderTraversal(root, result);
        return result;
    }

    private void inorderTraversal(TreeNode root, List<Integer> result) {
        if (root == null) return;

        inorderTraversal(root.left, result);
        result.add(root.val);
        inorderTraversal(root.right, result);
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
