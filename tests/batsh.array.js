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

Assert.equal(a[0], 18, '')
Assert.equal(a[1], 'y', '')
Assert.equal(a[2], 'abx', '')
Assert.equal(a[3], 1, '')
Assert.equal(a[4], '518', '')

a = [1, 2, 3];

Assert.equal(a[0], 1, '')
Assert.equal(a[1], 2, '')
Assert.equal(a[2], 3, '')


Assert.equal(("10" + a[0]) * 2, 202, '')
Assert.equal(len(a), 3, '')
Assert.equal(len(a) * 8, 24, '')
