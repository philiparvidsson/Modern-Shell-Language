include('assert.js')

function a(x, y) {
    assert.equal(x, 'hello', 'x should contain hello')
    assert.equal(y, 'world', 'y should contain world')
}

function b(x) {
    assert.equal(x, 'hello world', 'x should contain hello world')
}

function c() {
    return 'hello world'
}

function d() {
    return;

    // Should never happen since we return.
    assert.isTrue(false, 'return statement failed')
}

a('hello', 'world')
b('hello world')

assert.equal(c(), 'hello world', 'c() should return hello world')

b(c())
d()
