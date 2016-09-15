include ('assert.js')

/**
 * This test is taken from the Batsh test suite.
 *
 * See https://github.com/BYVoid/Batsh for more information.
 */

Assert.equal(false          ,  0 , 'batsh test failed 1')
Assert.equal(true           ,  1 , 'batsh test failed 2')
Assert.equal(42             ,  42, 'batsh test failed 3')
Assert.equal(1 + (4 + 6) * 3,  31, 'batsh test failed 4')
Assert.equal(8 - 3 % 2      ,  7 , 'batsh test failed 5')
Assert.equal(-9 - 9         , -18, 'batsh test failed 6')
Assert.equal((2 + 8) / 3    ,  3 , 'batsh test failed 7')
Assert.equal(2 ==/*=*/ 2    ,  1 , 'batsh test failed 8')
Assert.equal(6 !=/*=*/ 8    ,  1 , 'batsh test failed 9')
Assert.equal(3 > 2          ,  1 , 'batsh test failed 10')
Assert.equal(4 < 5          ,  1 , 'batsh test failed 11')
Assert.equal(6 >= 2         ,  1 , 'batsh test failed 12')
Assert.equal(19 <= 30       ,  1 , 'batsh test failed 13')
Assert.equal(!true          ,  0 , 'batsh test failed 14')
Assert.equal(!false         ,  1 , 'batsh test failed 15')
Assert.equal(!(2 - 1)       ,  0 , 'batsh test failed 16')
