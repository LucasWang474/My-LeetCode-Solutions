// 7. Reverse Integer
// https://leetcode.com/problems/reverse-integer/
function reverse(x: number): number {
  let res: number = 0;
  const sign = x >= 0 ? 1 : -1;
  x = Math.abs(x);

  while (x > 0) {
    res = res * 10 + x % 10;
    x = Math.floor(x / 10);
  }

  res = res * sign;
  if (res < (-2) ** 31 || res > 2 ** 31 - 1) {
    return 0;
  }
  return res;
}
