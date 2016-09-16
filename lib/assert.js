/*----------------------------------------------------------
 * INCLUDES
 *--------------------------------------------------------*/

include('stdio.js')
include('sys.js')

/*----------------------------------------------------------
 * NAMESPACE
 *--------------------------------------------------------*/

/**
 * Provides functionality for asserting certain conditions.
 */
function assert() {}

/*----------------------------------------------------------
 * FUNCTIONS
 *--------------------------------------------------------*/

/**
 * Tests if two values are equal. Exits with the specified error message
 * if they are not.
 *
 * @param a Actual value.
 * @param e Expected value-
 * @param s The error message.
 */
assert.equal = function (a, e, s) {
    if (a == e) return;

    println()
    println('assertion failed:', s)
    println('expected value:', e)
    println('actual value:', a)
    println('----------')

    exit(10001)
}

/**
 * Tests if the specified value is false. Exits with the specified error
 * message if it is not.
 *
 * @param a The value to check.
 * @param s The error message.
 */
assert.isFalse = function (a, s) {
    assert.equal(a ? true : false, false, s)
}

/**
 * Tests if the specified value is true. Exits with the specified error
 * message if it is not.
 *
 * @param a The value to check.
 * @param s The error message.
 */
assert.isTrue = function (a, s) {
    assert.equal(a ? true : false, true, s)
}
