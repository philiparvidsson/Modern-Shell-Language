include ('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

function len(a) { return a.length }

a = ["", "y", -1, 1];
a[0] = 2 * 9;
a[2] = "abx";
a[4] = "5" + a[0];

assert.equal(a[0], 18, '')
assert.equal(a[1], 'y', '')
assert.equal(a[2], 'abx', '')
assert.equal(a[3], 1, '')
assert.equal(a[4], '518', '')

a = [1, 2, 3];

assert.equal(a[0], 1, '')
assert.equal(a[1], 2, '')
assert.equal(a[2], 3, '')


assert.equal(("10" + a[0]) * 2, 202, '')
assert.equal(len(a), 3, '')
assert.equal(len(a) * 8, 24, '')
