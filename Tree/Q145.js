/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


/**
 * https://leetcode.com/problems/binary-tree-postorder-traversal/
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal1 = function (root) {
    if (!root) return [];
    return [...postorderTraversal(root.left), ...postorderTraversal(root.right), root.val];
};


/**
 * https://leetcode.com/problems/binary-tree-postorder-traversal/
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function (root) {
    const stack = [], res = [];
    while (root || stack.length > 0) {
        while (root) {
            stack.push(root.val);
            if (root.right) stack.push(root.right);
            root = root.left;
        }

        const cur = stack.pop();
        if (cur instanceof TreeNode) root = cur;
        else res.push(cur);
    }
    return res;
};
