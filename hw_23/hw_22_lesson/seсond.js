function createArray (amount) {
  let result = []
  for (let i = 0; i < amount / 3; i++) {
    result.push([i * 3 + 1, i * 3 + 2, i * 3 + 3])
  }
  console.log(result)
  return result
}

createArray(12)
// 0: (3) [1, 2, 3]
// 1: (3) [4, 5, 6]
// 2: (3) [7, 8, 9]
// 3: (3) [10, 11, 12]