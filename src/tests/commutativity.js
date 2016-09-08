include('tests/test.js')

test.name = "commutativity"

a = 2*(3 + 4)
b = (4 + 3)*2

assert.equal(a, 14, 'addition gave incorrect result')
assert.equal(b, 14, 'addition gave incorrect result')
