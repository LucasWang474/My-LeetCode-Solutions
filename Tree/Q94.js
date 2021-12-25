/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal1 = function (root) {
    if (!root) return [];
    return [...inorderTraversal(root.left), root.val, ...inorderTraversal(root.right)];
};

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
    const stack = [], res = [];
    while (root || stack.length > 0) {
        while (root) {
            if (root.right) stack.push(root.right);
            stack.push(root.val);
            root = root.left;
        }

        const cur = stack.pop();
        if (cur instanceof TreeNode) root = cur;
        else res.push(cur);
    }
    return res;
};
