/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}


/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function (root, targetSum) {
    function dfs(cur, sumSoFar, pathSoFar) {
        if (!cur) return;
        if (!cur.left && !cur.right) {
            if (cur.val + sumSoFar === targetSum) {
                res.push([...pathSoFar, cur.val]);
            }

        }

        sumSoFar += cur.val;
        pathSoFar.push(cur.val);
        dfs(cur.left, sumSoFar, pathSoFar);
        dfs(cur.right, sumSoFar, pathSoFar);
        pathSoFar.pop();
    }

    let res = [];
    dfs(root, 0, []);
    return res;
};
