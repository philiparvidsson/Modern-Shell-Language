include('inc/testing.js')

test.name = 'recursion test'

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

assert.areEqual(fac(0), 1  , 'recursion failed 1')
assert.areEqual(fac(1), 1  , 'recursion failed 2')
assert.areEqual(fac(2), 2  , 'recursion failed 3')
assert.areEqual(fac(3), 6  , 'recursion failed 4')
assert.areEqual(fac(4), 24 , 'recursion failed 5')
assert.areEqual(fac(5), 120, 'recursion failed 6')

assert.areEqual(fib(0), 0, 'recursion failed 7')
assert.areEqual(fib(1), 1, 'recursion failed 8')
assert.areEqual(fib(2), 1, 'recursion failed 9')
assert.areEqual(fib(3), 2, 'recursion failed 10')
assert.areEqual(fib(4), 3, 'recursion failed 11')
assert.areEqual(fib(5), 5, 'recursion failed 12')
