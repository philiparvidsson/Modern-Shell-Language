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

assert.equal(fac(0), 1  , 'recursion failed 1')
assert.equal(fac(1), 1  , 'recursion failed 2')
assert.equal(fac(2), 2  , 'recursion failed 3')
assert.equal(fac(3), 6  , 'recursion failed 4')
assert.equal(fac(4), 24 , 'recursion failed 5')
assert.equal(fac(5), 120, 'recursion failed 6')

assert.equal(fib(0), 0, 'recursion failed 7')
assert.equal(fib(1), 1, 'recursion failed 8')
assert.equal(fib(2), 1, 'recursion failed 9')
assert.equal(fib(3), 2, 'recursion failed 10')
assert.equal(fib(4), 3, 'recursion failed 11')
assert.equal(fib(5), 5, 'recursion failed 12')
