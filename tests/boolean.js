include('inc/testing.js')

test.name = "boolean operations test"

f = false
t = true

assert.isFalse(0   , 'zero should be falsy')
assert.isTrue(1    , 'non-zero should be truthy 1')
assert.isTrue(0-1  , 'non-zero should be truthy 2')
assert.isTrue(500  , 'non-zero should be truthy 3')
assert.isTrue(0-500, 'non-zero should be truthy 4')

assert.areEqual( f, false, 'f should equal false')
assert.areEqual( t, true , 't should equal true')
assert.areEqual(!f, true , 'not f should equal true')
assert.areEqual(!t, false, 'not t should equal false')

assert.areEqual(f == false, true , 'f equals false should be true')
assert.areEqual(f == true , false, 'f equals true should be false')

assert.areEqual(t == false, false, 't equals false should be false')
assert.areEqual(t == true , true , 't equals true should be true')

// do some more stuff here with relative comparisons etc
