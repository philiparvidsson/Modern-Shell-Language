include('test.js')

test.name = "boolean operations"

f = false
t = true

assert.equal(f, false, 'f should equal false')
assert.equal(t, true , 't should equal true')

assert.equal(f == false, true , 'f equals false should be true')
assert.equal(f == true , false, 'f equals true should be false')

assert.equal(t == false, false, 't equals false should be false')
assert.equal(t == true , true , 't equals true should be true')

// do some more stuff here with relative comparisons etc
