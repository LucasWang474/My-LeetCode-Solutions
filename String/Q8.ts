function myAtoi(s: string): number {
  let res = parseInt(s.trim()) || 0;
  if (res > 2 ** 31 - 1) {
    res = 2 ** 31 - 1;
  } else if (res < (-2) ** 31) {
    res = (-2) ** 31;
  }
  return res;
}
