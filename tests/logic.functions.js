include('assert.js')

function a(x, y) {
    Assert.equal(x, 'hello', 'x should contain hello')
    Assert.equal(y, 'world', 'y should contain world')
}

function b(x) {
    Assert.equal(x, 'hello world', 'x should contain hello world')
}

function c() {
    return 'hello world'
}

function d() {
    return;

    // Should never happen since we return.
    Assert.isTrue(false, 'return statement failed')
}

a('hello', 'world')
b('hello world')

Assert.equal(c(), 'hello world', 'c() should return hello world')

b(c())
d()
