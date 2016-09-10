include('inc/testing.js')

test.name = "commutativity test"

a = 2*(3 + 4)
b = (4 + 3)*2

assert.areEqual(a, 14, 'addition gave incorrect result')
assert.areEqual(b, 14, 'addition gave incorrect result')
