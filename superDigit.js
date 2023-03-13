function superDigit(n, k) {
  while (n.length > 1) {
    n = sumDigits(n);
  }
  let superDigit = parseInt(n) * k;
  if (superDigit > 10) {
    superDigit = parseInt(sumDigits(String(superDigit)));
  }
  return superDigit;
}

function sumDigits(num) {
  let arr = num.split("");
  let sum = 0;
  while (arr.length > 0) {
    sum += parseInt(arr.pop());
  }
  return String(sum);
}

console.log(superDigit("148", 3));
// console.log(sumDigits("9875987598759875"));
