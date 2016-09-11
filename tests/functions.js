include('inc/testing.js')

test.name = 'functions test'

function a(x, y) {
    assert.areEqual(x, 'hello', 'x should contain hello')
    assert.areEqual(y, 'world', 'y should contain world')
}

function b(x) {
    assert.areEqual(x, 'hello world', 'x should contain hello world')
}

function c() {
    return 'hello world'
}

function d() {
    return;

    // Should never happen since we return.
    test.fail()
}

a('hello', 'world')
b('hello world')

assert.areEqual(c(), 'hello world', 'c() should return hello world')

b(c())
d()
