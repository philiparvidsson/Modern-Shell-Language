assert = []
test   = []

assert.equal = function (a, b, s) {
    if (a != b) {
        console.log('assertion failed:', s)
        console.log('expected value:', b)
        console.log('actual value:', a)
        test.fail()
    }

    return true
}

test.fail = function () {
    console.log(test.name, 'failed')
    process.exit()
}

test.name = 'missing name'
