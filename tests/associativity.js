include('tests/test.js')

test.name = "associativity"

a = 2*3 + 4
b = 4 + 3*2

assert.equal(a, 10, 'multiplication gave incorrect result')
assert.equal(b, 10, 'multiplication gave incorrect result')
