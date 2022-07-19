// https://leetcode.com/problems/zigzag-conversion/
function convert(s: string, numRows: number): string {
  if (numRows === 1) return s;

  const rows: string[][] = [];
  for (let i = 0; i < numRows; i++) {
    rows[i] = [];
  }

  const STEP1 = 2 * numRows - 2;

  for (let i = 0; i < s.length; i++) {
    const mod = i % STEP1;
    if (mod < numRows) {
      rows[mod].push(s[i]);
    } else {
      const j = numRows - 1 - (mod - numRows) - 1;
      rows[j].push(s[i]);
    }
  }

  let res = '';
  for (let row of rows) {
    res += row.join('');
  }
  return res;
}
