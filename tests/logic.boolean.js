include('assert.js')

f = false
t = true

assert.isFalse(0   , 'zero should be falsy')
assert.isTrue(1    , 'non-zero should be truthy 1')
assert.isTrue(0-1  , 'non-zero should be truthy 2')
assert.isTrue(500  , 'non-zero should be truthy 3')
assert.isTrue(0-500, 'non-zero should be truthy 4')

assert.isFalse(!!false, 'not not false should be falsy')
assert.isFalse(!123   , 'not 123 should be falsy')
assert.isFalse(!true  , 'not true should be falsy')
assert.isTrue(!!true  , 'not not true should be truthy')
assert.isTrue(!0      , 'not zero should be truthy')
assert.isTrue(!false  , 'not false should be truthy')

assert.equal( f, false, 'f should equal false')
assert.equal( t, true , 't should equal true')
assert.equal(!f, true , 'not f should equal true')
assert.equal(!t, false, 'not t should equal false')

assert.equal(f == false, true , 'f equals false should be true')
assert.equal(f == true , false, 'f equals true should be false')

assert.equal(t == false, false, 't equals false should be false')
assert.equal(t == true , true , 't equals true should be true')

// do some more stuff here with relative comparisons etc
