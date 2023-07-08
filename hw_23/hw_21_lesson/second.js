// первый способ

function factorial_recursive(number) {
    return (number > 1) ? number * factorial_recursive(number - 1) : 1
}

/*
factorial_recursive(7)
5040
factorial_recursive(6)
720
 */

// второй способ, используя изначально заготовленный массив
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let result = 1
const newArray = numbers.map((item) => result *= item)
console.log(result)