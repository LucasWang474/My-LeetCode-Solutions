/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * https://leetcode.com/problems/count-complete-tree-nodes/
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function (root) {
    if (!root) return 0;

    const LH = height(root.left), RH = height(root.right);
    if (LH === RH) {
        return 1 + Math.trunc(2 ** LH - 1) + countNodes(root.right);
    } else {
        return 1 + countNodes(root.left) + Math.trunc(2 ** RH - 1);
    }
};


function height(root) {
    let res = 0;
    while (root) {
        root = root.left;
        res += 1;
    }
    return res;
}
