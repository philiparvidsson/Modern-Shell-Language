include('assert.js')

f = false
t = true

Assert.isFalse(0   , 'zero should be falsy')
Assert.isTrue(1    , 'non-zero should be truthy 1')
Assert.isTrue(0-1  , 'non-zero should be truthy 2')
Assert.isTrue(500  , 'non-zero should be truthy 3')
Assert.isTrue(0-500, 'non-zero should be truthy 4')

Assert.isFalse(!!false, 'not not false should be falsy')
Assert.isFalse(!123   , 'not 123 should be falsy')
Assert.isFalse(!true  , 'not true should be falsy')
Assert.isTrue(!!true  , 'not not true should be truthy')
Assert.isTrue(!0      , 'not zero should be truthy')
Assert.isTrue(!false  , 'not false should be truthy')

Assert.equal( f, false, 'f should equal false')
Assert.equal( t, true , 't should equal true')
Assert.equal(!f, true , 'not f should equal true')
Assert.equal(!t, false, 'not t should equal false')

Assert.equal(f == false, true , 'f equals false should be true')
Assert.equal(f == true , false, 'f equals true should be false')

Assert.equal(t == false, false, 't equals false should be false')
Assert.equal(t == true , true , 't equals true should be true')

// do some more stuff here with relative comparisons etc
