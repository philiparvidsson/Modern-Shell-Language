include ('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

assert.equal(false          ,  0 , 'batsh test failed 1')
assert.equal(true           ,  1 , 'batsh test failed 2')
assert.equal(42             ,  42, 'batsh test failed 3')
assert.equal(1 + (4 + 6) * 3,  31, 'batsh test failed 4')
assert.equal(8 - 3 % 2      ,  7 , 'batsh test failed 5')
assert.equal(-9 - 9         , -18, 'batsh test failed 6')
assert.equal((2 + 8) / 3    ,  3 , 'batsh test failed 7')
assert.equal(2 ==/*=*/ 2    ,  1 , 'batsh test failed 8')
assert.equal(6 !=/*=*/ 8    ,  1 , 'batsh test failed 9')
assert.equal(3 > 2          ,  1 , 'batsh test failed 10')
assert.equal(4 < 5          ,  1 , 'batsh test failed 11')
assert.equal(6 >= 2         ,  1 , 'batsh test failed 12')
assert.equal(19 <= 30       ,  1 , 'batsh test failed 13')
assert.equal(!true          ,  0 , 'batsh test failed 14')
assert.equal(!false         ,  1 , 'batsh test failed 15')
assert.equal(!(2 - 1)       ,  0 , 'batsh test failed 16')
