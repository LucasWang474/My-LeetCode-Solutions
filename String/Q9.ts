function isPalindrome(x: number): boolean {
  let s = String(x);
  return s === s.split('').reverse().join('');
}
