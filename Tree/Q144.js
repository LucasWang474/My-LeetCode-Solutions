/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


/**
 * https://leetcode.com/problems/binary-tree-preorder-traversal/
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal1 = function (root) {
    if (!root) return [];
    return [root.val, ...preorderTraversal(root.left), ...preorderTraversal(root.right)];
};


/**
 * https://leetcode.com/problems/binary-tree-preorder-traversal/
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function (root) {
    const stack = [], res = [];
    while (root || stack.length > 0) {
        while (root) {
            res.push(root.val);
            if (root.right) stack.push(root.right);
            root = root.left;
        }
        root = stack.pop();
    }
    return res;
};
