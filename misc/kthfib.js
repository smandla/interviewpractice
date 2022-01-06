/**
 * n = 3
 * 1, 1, 2, 3, 5, 8, 13, 21, 34
 * 1, 2, 3, 4, 5, 6, 7
 */
const kthfib = function (n) {
  let a = 0;
  let b = 1;
  let c = 0;
  if (n <= 2) {
    return 1;
  }
  console.log("n", n + 1);
  for (let i = 1; i < n; i++) {
    c = a + b;
    a = b;
    b = c;
  }
  return c;
};

console.log(kthfib(8));

/**
 * time complexity - O(n) -> contains one loop
 * space complexity - O(1) -> constant space
 */
