function gridChallenge(grid) {
  let orderedGrid = [];
  for (let i = 0; i < grid.length; i++) {
    orderedGrid.push(grid[i].split("").sort().join(""));
  }
  let areColumnsSorted = "YES";

  for (let i = 0; i < orderedGrid.length; i++) {
    for (let j = 0; j < orderedGrid.length; j++) {
      let nextValue = i + 1;
      if (nextValue === orderedGrid.length) {
        break;
      }
      if (orderedGrid[i][j] > orderedGrid[nextValue][j]) {
        areColumnsSorted = "NO";
        break;
      }
    }
  }
  return areColumnsSorted;
}

console.log(gridChallenge(["kc", "iu"]));
