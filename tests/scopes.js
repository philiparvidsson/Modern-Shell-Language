include('inc/testing.js')

test.name = 'scopes test'

// Test access to global/outer scopes.
a = '123'
function b() {
    assert.areEqual(a, '123', 'could not access global var a')

    c = 'xyz'

    function d() {
        assert.areEqual(c, 'xyz', 'could not access outer scope var c')
    }

    d()
}

b()
