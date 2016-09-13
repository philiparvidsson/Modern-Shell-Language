assert = []
test   = []

assert.areEqual = function (a, b, s) {
    if (a == b)
        return false

    console.log()
    console.log('----------')
    console.log('assertion failed:', s)
    console.log('expected value:', b)
    console.log('actual value:', a)
    test.fail()

    return true
}

test.fail = function () {
    console.log(test.name, 'failed')
    process.exit(1)
}

assert.isFalse = function (a, s) {
    b = a ? true : false
    assert.areEqual(b, false, s)
}

assert.isTrue = function (a, s) {
    b = a ? true : false
    assert.areEqual(b, true, s)
}

test.name = 'missing name'
