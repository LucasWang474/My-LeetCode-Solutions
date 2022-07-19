/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  const N = matrix.length;

  const rotated: number[][] = [];
  for (let col = 0; col < N; col++) {
    rotated.push([]);
    let resLen = rotated.length;
    for (let row = 0; row < N; row++) {
      rotated[resLen - 1].push(matrix[row][col]);
    }
    rotated[resLen - 1].reverse();
  }

  for (let row = 0; row < N; row++) {
    for (let col = 0; col < N; col++) {
      matrix[row][col] = rotated[row][col];
    }
  }
}
