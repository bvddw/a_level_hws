function sumOfTwoMin (array) {
  let min1 = array[0]
  let min2 = array[1]
  if (min1 > min2) {
    min1 = min1 + min2
    min2 = min1 - min2
    min1 = min1 - min2
  }
  array.map((item) => {
    if (min1 > item) {
      min2 = min1
      min1 = item
    }
  })
  return min1 + min2
}

sumOfTwoMin([19, 5, 42, 2, 77]) // 7