include('stdio.js')

/**
 * Provides functionality for asserting certain conditions.
 */
Assert = function () {}

/**
 * Tests if two values are equal. Exits with the specified error message
 * if they are not.
 *
 * @param a First value.
 * @param b Second value.
 * @param s The error message.
 */
Assert.equal = function (a, b, s) {
    if (a == b) return;

    println()
    println('----------')
    println('assertion failed:', s)
    println('expected value:', b)
    println('actual value:', a)

    process.exit()
}

/**
 * Tests if the specified value is false. Exits with the specified error
 * message if it is not.
 *
 * @param a The value to check.
 * @param s The error message.
 */
Assert.isFalse = function (a, s) {
    Assert.equal(a ? true : false, false, s)
}

/**
 * Tests if the specified value is true. Exits with the specified error
 * message if it is not.
 *
 * @param a The value to check.
 * @param s The error message.
 */
Assert.isTrue = function (a, s) {
    Assert.equal(a ? true : false, true, s)
}
