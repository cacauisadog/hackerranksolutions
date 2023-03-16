function isValid(s) {
  const frequencyMap = new Map();

  for (let c of s) {
    if (frequencyMap.has(c)) {
      let n = frequencyMap.get(c);
      frequencyMap.set(c, n + 1);
    } else {
      frequencyMap.set(c, 1);
    }
  }

  let firstValue;
  let removed = false;
  for (const v of frequencyMap.values()) {
    if (!firstValue) firstValue = v;
    else if (firstValue !== v) {
      if ((v === 1 || v === firstValue + 1) && !removed) {
        removed = true;
      } else return "NO";
    }
  }
  return "YES";
}

console.log(isValid("aabcd"));
