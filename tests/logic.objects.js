include('assert.js')

// Testing complex objects here!

// 1. Object properties
a = []
a.prop = 'foo'

assert.equal(a.prop, 'foo', 'object properties not working')

// 2. Passing objects to functions
b = []
b.some_prop = 'bar'
c = function (o) {
    assert.equal(o.some_prop, 'bar')
}
c(b)

// 3. Mutating objects in functions
d = []
e = function (o) { o.the_prop = 'hello world' }
e(d)

assert.equal(d.the_prop, 'hello world', 'object mutation in function failed')

// 4. Returning objects from functions
f = function() {
    g = []
    g.a_prop = 'world hello'

    return g
}

h = f()
i = f()

assert.equal(h.a_prop, 'world hello', 'object returning failed 1')
// FIXME: Syntax not yet supported.
//assert.equal(f().a_prop, 'world hello', 'object returning failed 2')

h.test_prop = '123'
i.test_prop = 'abc'

// h and i should not point to the same object since we instantiated two objects
// with two calls to f()
assert.equal(h.test_prop, '123', 'object reference error 1')
assert.equal(i.test_prop, 'abc', 'object reference error 2')

// 5. Nested objects

j = []
j.nested = []
j.nested.func = function () { return 12345 }

assert.equal(j.nested.func(), 12345, 'nested objects not working properly')

// 6. Self-referencing objects (this keyword, kind of)
// FIXME: Implement this-keyword

function k() {
    obj = []

    obj.value = 0

    obj.test_func = function () {
        return obj.value
    }

    return obj
}

l = k()
m = k()

l.value = 444
m.value = 777

assert.equal(l.test_func(), 444, 'self-reference failed 1')
assert.equal(m.test_func(), 777, 'self-reference failed 2')

// 7. Objects inside arrays (with 'ctor' args)

n = function (x) {
    o = []

    o.val = x

    return o
}

p = [n('xyz'), n('pqr')]

assert.equal(p[0].val, 'xyz', 'object in array failed 1')
assert.equal(p[1].val, 'pqr', 'object in array failed 2')
