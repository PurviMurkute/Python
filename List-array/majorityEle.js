list = [1, 1, 2, 1, 3, 5, 1];

console.log(Math.floor(7 / 2));

function majorityEle(arr) {
  let n = arr.length;
  seen = {};
  uniqueArr = new Set(arr);

  for (let i = 0; i < n; i++) {
    if (arr[i] in seen) {
      seen[arr[i]] += 1;
    } else {
      seen[arr[i]] = 1;
    }
  }

  uniqueArr.for((n) => {
    if (seen[num] > Math.floor(n / 2)) {
      return num;
    }
  });
  return -1;
}

console.log(majorityEle(list));
