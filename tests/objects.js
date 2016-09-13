include('inc/testing.js')

// Testing complex objects here!

// 1. Object properties
a = []
a.prop = 'foo'

assert.areEqual(a.prop, 'foo', 'object properties not working')

// 2. Passing objects to functions
b = []
b.some_prop = 'bar'
c = function (o) {
    assert.areEqual(o.some_prop, 'bar')
}
c(b)

// 3. Mutating objects in functions
d = []
e = function (o) { o.the_prop = 'hello world' }
e(d)

assert.areEqual(d.the_prop, 'hello world', 'object mutation in function failed')

// 4. Returning objects from functions
f = function() {
    g = []
    g.a_prop = 'world hello'

    return g
}

h = f()
i = f()

assert.areEqual(h.a_prop, 'world hello', 'object returning failed 1')
//assert.areEqual(f().a_prop, 'world hello', 'object returning failed 2')

h.test_prop = '123'
i.test_prop = 'abc'

// h and i should not point to the same object since we instantiated two objects
// with two calls to f()
assert.areEqual(h.test_prop, '123', 'object reference error 1')
assert.areEqual(i.test_prop, 'abc', 'object reference error 2')

// 4. Nested objects

j = []
j.nested = []
j.nested.func = function () { return 12345 }

assert.areEqual(j.nested.func(), 12345, 'nested objects not working properly')
