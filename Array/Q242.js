/**
 * https://leetcode.com/problems/valid-anagram/
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
// Time: O(NlogN)
var isAnagram = function (s, t) {
    return [...s].sort().join('') === [...t].sort().join('');
};

// Time: O(N)
var isAnagram2 = function (s, t) {
    if (s.length !== t.length) return false;

    const map = new Map();
    for (let char of s) {
        map.set(char, (map.get(char) || 0) + 1);
    }
    for (let char of t) {
        if (!map.has(char)) return false;
        if (map.get(char) <= 0) return false;
        map.set(char, map.get(char) - 1);
    }
    for (let value of map.values()) {
        if (value !== 0) return false;
    }
    return true;
};
