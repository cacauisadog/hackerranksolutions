function balancedSums(arr) {
  let arrLen = arr.length;

  if (arrLen === 1) return "YES";
  if (arr[0] === 0 && arr[1] === 0) return "YES";
  if (arr[arrLen - 1] === 0 && arr[arrLen - 2] === 0) return "YES";

  let sum = (arr) => arr.reduce((a, b) => a + b, 0);

  let initialLeftArray = arr.slice(0, 1);
  let initialRightArray = arr.slice(2, arrLen);
  let left = sum(initialLeftArray);
  let right = sum(initialRightArray);

  if (left === right) return "YES";

  for (let i = 2; i < arrLen; i++) {
    left += arr[i - 1];
    right -= arr[i];
    if (left === right) return "YES";
  }

  return "NO";
}

console.log(balancedSums([1]));
console.log(balancedSums([2]));
console.log(balancedSums([3]));
console.log(balancedSums([1, 2]));
console.log(balancedSums([1, 4, 1]));
console.log(balancedSums([1, 5, 1]));
console.log(balancedSums([234]));
console.log(balancedSums([20000]));
console.log(balancedSums([6, 23, 6]));
console.log(balancedSums([1]));
