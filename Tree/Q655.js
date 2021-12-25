/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


/**
 * https://leetcode.com/problems/print-binary-tree/
 * @param {TreeNode} root
 * @return {string[][]}
 */
var printTree = function (root) {
    function getHeight(cur) {
        if (!cur) return 0;
        return 1 + Math.max(getHeight(cur.left), getHeight(cur.right));
    }

    let height = getHeight(root), width = 2 ** height - 1;
    let res = new Array(height);
    for (let i = 0; i < res.length; i++) {
        res[i] = new Array(width).fill('');
    }

    function fillRes(cur, depth, left, right) {
        if (!cur) return;

        let mid = left + ((right - left) >> 1);
        res[depth][mid] += cur.val;
        fillRes(cur.left, depth + 1, left, mid - 1);
        fillRes(cur.right, depth + 1, mid + 1, right);
    }

    fillRes(root, 0, 0, width - 1);

    return res;
};
