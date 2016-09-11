include('inc/testing.js')

function a(x, y) {
    assert.areEqual(x, 'hello', 'x should contain hello')
    assert.areEqual(y, 'world', 'y should contain world')
}

function b(x, y) {
    assert.areEqual(x, 'hello world', 'x should contain hello world')
}

function c() {
    return 'hello world'
}

a('hello', 'world')
b('hello world')

assert.areEqual(c(), 'hello world', 'c() should return hello world')

b(c())
