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
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
    if (!root) return [];

    let hasNextLevel = true;
    const allLevels = [[root]];
    while (hasNextLevel) {
        const curLevel = allLevels[allLevels.length - 1];
        const nextLevel = [];
        for (let node of curLevel) {
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        hasNextLevel = nextLevel.length > 0;
        if (hasNextLevel) allLevels.push(nextLevel);
    }

    allLevels.reverse(); // NONSENSE
    return allLevels.map(curLevel => curLevel.map(node => node.val));
};
