include('assert.js')

// Test access to global/outer scopes.
a = '123'
function b() {
    assert.equal(a, '123', 'could not read global var a')
    a = 'pqr'
    assert.equal(a, 'pqr', 'could not mutate global var a')

    c = 'xyz'

    // FIXME: nested functions may not be named
    d = function () {
        assert.equal(c, 'xyz', 'could not access outer scope var c')
    }

    d()
}

b()
