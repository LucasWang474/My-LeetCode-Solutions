/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


/**
 * https://leetcode.com/problems/diameter-of-binary-tree/
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree1 = function (root) {
    function getHeight(cur) {
        if (!cur) return 0;

        const LH = getHeight(cur.left), RH = getHeight(cur.right);
        maxDiameter = Math.max(maxDiameter, LH + RH);

        return 1 + Math.max(LH, RH);
    }

    let maxDiameter = 0;
    getHeight(root);
    return maxDiameter;
};


var diameterOfBinaryTree = function (root) {
    /**
     * Returns the height of a tree.
     * A tree with a single node is of height 1.
     */
    function getHeight(cur) {
        if (!cur) return 0; // The end of tree, height is 0

        const leftHeight = getHeight(cur.left);
        const rightHeight = getHeight(cur.right);

        const curDiameter = leftHeight + rightHeight;
        maxDiameter = Math.max(maxDiameter, curDiameter);

        return 1 + Math.max(leftHeight, rightHeight);
    }

    let maxDiameter = 0;
    getHeight(root);
    return maxDiameter;
};
