/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


/**
 * https://leetcode.com/problems/binary-tree-level-order-traversal/
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    if (!root) return [];

    const allLevels = [];
    let queue = [root];
    while (queue.length > 0) {
        const curLevel = [], newQueue = [];
        for (let node of queue) {
            curLevel.push(node.val);
            if (node.left) newQueue.push(node.left);
            if (node.right) newQueue.push(node.right);
        }
        allLevels.push(curLevel);
        queue = newQueue;
    }
    return allLevels;
};
