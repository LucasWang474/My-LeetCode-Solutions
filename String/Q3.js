// /**
//  * @param {string} s
//  * @return {number}
//  */
// var lengthOfLongestSubstring = function(s) {
//     let maxLen = 0;
//     for (let i = 0; i < s.length; i++) {
//         const seen = new Set();

//         let j = i;
//         while (j < s.length) {
//             const cur = s[j];
//             if (seen.has(cur)) break;
//             seen.add(cur);
//             j++;
//         }

//         maxLen = Math.max(maxLen, j - i);
//     }
//     return maxLen;
// };


/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(str) {
  let maxLen = 0, L = 0;
  const set = new Set();
  
  for (let R = 0; R < str.length; R++) {
    while (set.has(str[R])) {
      set.delete(str[L]);
      L++;
    }
    
    set.add(str[R]);
    maxLen = Math.max(maxLen, R - L + 1);
  }
  
  return maxLen;
};
