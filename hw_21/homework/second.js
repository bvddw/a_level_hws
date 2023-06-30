function factorial_recursive(number) {
    return (number > 1) ? number * factorial_recursive(number - 1) : 1
}

/*
factorial_recursive(7)
5040
factorial_recursive(6)
720
 */

function factorial_no_recursive(number) {
    let product = 1
    for (let i = 1; i < number + 1; i++) {
        product *= i
    }
    return product
}

/*
factorial_no_recursive(12)
479001600
factorial_no_recursive(7)
5040
factorial_no_recursive(6)
720
 */
