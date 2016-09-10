include('inc/testing.js')

test.name = "associativity test"

a = 2*3 + 4
b = 4 + 3*2

assert.areEqual(a, 10, 'multiplication gave incorrect result')
assert.areEqual(b, 10, 'multiplication gave incorrect result')
