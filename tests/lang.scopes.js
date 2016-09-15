include('assert.js')

// Test access to global/outer scopes.
a = '123'
function b() {
    Assert.equal(a, '123', 'could not read global var a')
    a = 'pqr'
    Assert.equal(a, 'pqr', 'could not mutate global var a')

    c = 'xyz'

    // FIXME: nested functions may not be named
    d = function () {
        Assert.equal(c, 'xyz', 'could not access outer scope var c')
    }

    d()
}

b()
