include('assert.js')

a = 27

assert.equal(a+1  , 28 , 'addition gave incorrect result')
assert.equal(a-30 , 0-3, 'subtraction gave incorrect result')
assert.equal(a*11 , 297, 'multiplication gave incorrect result')
assert.equal(a/3  , 9  , 'division gave incorrect result')
assert.equal(a%7  , 6  , 'modulo gave incorrect result')
assert.equal(a<<3 , 216, 'left-shift gave incorrect result')
assert.equal(a>>1 , 13 , 'right-shift gave incorrect result')
assert.equal(a&49 , 17 , 'bitwise and gave incorrect result')
assert.equal(a|23 , 31 , 'bitwise or gave incorrect result')
assert.equal(a^23 , 12 , 'bitwise xor gave incorrect result')

b=a
assert.equal(b++  , 27 , 'post-increment gave incorrect result')

c=a
assert.equal(c--  , 27 , 'post-decrement gave incorrect result')

d = 11
e = 13
assert.isTrue (d <  e, 'd should be less than e')
assert.isTrue (d <= e, 'd should be less than or equal to e')
assert.isTrue (d != e, 'd should be unequal to e')
assert.isFalse(d >  e, 'd should not be greater than e')
assert.isFalse(d >= e, 'd should not be greater than or equal to e')
assert.isFalse(d == e, 'd should not be equal to e')
