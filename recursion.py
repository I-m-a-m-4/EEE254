/**
 * Recursively converts a non-negative integer to its binary string.
 *
 * @param {number} n – the integer to convert (n ≥ 0)
 * @returns {string} – binary representation of n
 */
function toBinary(n) {
  // Base case: if n is 0 or 1, we already know its binary
  if (n < 2) {
    return String(n);          // “0” or “1”
  }

  // Recursive case:
  // 1. Divide n by 2 (floor), convert that smaller number
  // 2. Append the remainder (n % 2) as the next binary digit
  //
  // This builds the binary string from the most significant bit down.
  return toBinary(Math.floor(n / 2)) + (n % 2);
}

// Example usage:
console.log(toBinary(0));   // → "0"
console.log(toBinary(5));   // → "101"
console.log(toBinary(10));  // → "1010"
console.log(toBinary(47));  // → "101111"
