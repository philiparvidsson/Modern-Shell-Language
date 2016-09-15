include('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

a = "Value: " + 1+(4+6)*3;
Assert.equal(a, 'Value: 31', '')
b = 3 + 4;
Assert.equal(b, 7, '')
c = a;
Assert.equal(c, 'Value: 31', '')
d = b + c;
Assert.equal(d, '7Value: 31', '')
