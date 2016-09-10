include('inc/testing.js')

test.name = "integer operations test"

a = 27

assert.areEqual(a+1  , 28 , 'addition gave incorrect result')
assert.areEqual(a-30 , 0-3, 'subtraction gave incorrect result')
assert.areEqual(a*11 , 297, 'multiplication gave incorrect result')
assert.areEqual(a/3  , 9  , 'division gave incorrect result')
assert.areEqual(a%7  , 6  , 'modulo gave incorrect result')
assert.areEqual(a<<3 , 216, 'left-shift gave incorrect result')
assert.areEqual(a>>1 , 13 , 'right-shift gave incorrect result')
assert.areEqual(a&49 , 17 , 'bitwise and gave incorrect result')
assert.areEqual(a|23 , 31 , 'bitwise or gave incorrect result')
assert.areEqual(a^23 , 12 , 'bitwise xor gave incorrect result')

b=a
assert.areEqual(b++  , 27 , 'post-increment gave incorrect result')

c=a
assert.areEqual(c--  , 27 , 'post-decrement gave incorrect result')
