assert = []
test   = []

assert.areEqual = function (a, b, s) {
    if (a != b) {
        console.log()
        console.log('----------')
        console.log('assertion failed:', s)
        console.log('expected value:', b)
        console.log('actual value:', a)
        test.fail()
    }

    return true
}

test.fail = function () {
    console.log(test.name, 'failed')
    process.exit(1)
}

assert.isFalse = function (a, s) {
    assert.areEqual(a, false, s)
}

assert.isTrue = function (a, s) {
    assert.areEqual(a, true, s)
}

test.name = '<missing name>'
