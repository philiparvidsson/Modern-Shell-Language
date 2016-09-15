include('assert.js')

function fac(x) {
    return x ? x*fac(x-1)
             : 1
}

function fib(x)  {
    if (x == 0)
        return 0
    else if (x == 1)
        return 1


    // Have to multiply by 1 to cast to ints. :(
    return 1*fib(x-1) + 1*fib(x-2)
}

Assert.equal(fac(0), 1  , 'recursion failed 1')
Assert.equal(fac(1), 1  , 'recursion failed 2')
Assert.equal(fac(2), 2  , 'recursion failed 3')
Assert.equal(fac(3), 6  , 'recursion failed 4')
Assert.equal(fac(4), 24 , 'recursion failed 5')
Assert.equal(fac(5), 120, 'recursion failed 6')

Assert.equal(fib(0), 0, 'recursion failed 7')
Assert.equal(fib(1), 1, 'recursion failed 8')
Assert.equal(fib(2), 1, 'recursion failed 9')
Assert.equal(fib(3), 2, 'recursion failed 10')
Assert.equal(fib(4), 3, 'recursion failed 11')
Assert.equal(fib(5), 5, 'recursion failed 12')
