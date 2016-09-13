
// Test access to global/outer scopes.
a = '123'
function b() {
    console.log('a is', a)

    c = 'xyz'

    function d() {
        console.log('c is', c)
    }

    d()
}

b()
