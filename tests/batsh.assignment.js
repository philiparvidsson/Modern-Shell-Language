include('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

a = "Value: " + 1+(4+6)*3;
assert.equal(a, 'Value: 31', '')
b = 3 + 4;
assert.equal(b, 7, '')
c = a;
assert.equal(c, 'Value: 31', '')
d = b + c;
assert.equal(d, '7Value: 31', '')
