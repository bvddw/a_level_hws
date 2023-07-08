function binToDec (array) {
  let summa = 0
  array.map((item, index) => summa += item * 2 ** (array.length - index - 1))
  return summa
}

binToDec([1, 0, 0, 0, 1]) // 17