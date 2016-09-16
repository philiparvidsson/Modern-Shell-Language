include('assert.js')
include('string.js')

s = string('hello world')

assert.equal(s.length(), 11, 'string length is wrong 1')

assert.equal(s.charAt( 0), 'h', 'charAt failed 1')
assert.equal(s.charAt( 1), 'e', 'charAt failed 2')
assert.equal(s.charAt( 2), 'l', 'charAt failed 3')
assert.equal(s.charAt( 3), 'l', 'charAt failed 4')
assert.equal(s.charAt( 4), 'o', 'charAt failed 5')
assert.equal(s.charAt( 5), ' ', 'charAt failed 6')
assert.equal(s.charAt( 6), 'w', 'charAt failed 7')
assert.equal(s.charAt( 7), 'o', 'charAt failed 8')
assert.equal(s.charAt( 8), 'r', 'charAt failed 9')
assert.equal(s.charAt( 9), 'l', 'charAt failed 10')
assert.equal(s.charAt(10), 'd', 'charAt failed 11')

assert.equal(s.substr(0, 1), 'h', 'substr failed 1')
assert.equal(s.substr(1, 2), 'el', 'substr failed 2')
assert.equal(s.substr(2, 3), 'llo', 'substr failed 3')
assert.equal(s.substr(3, 4), 'lo w', 'substr failed 4')

assert.equal(s.indexOf('h'), 0, 'indexOf failed 1')
assert.equal(s.indexOf('h', 0), 0, 'indexOf failed 2')
assert.equal(s.indexOf('e'), 1, 'indexOf failed 3')
assert.equal(s.indexOf('e', 0), 1, 'indexOf failed 4')
assert.equal(s.indexOf('l'), 2, 'indexOf failed 5')
assert.equal(s.indexOf('l', 3), 3, 'indexOf failed 6')

assert.equal(s.str(), 'hello world', 'str failed')

s = s.concat(' foo 123')

assert.equal(s.length(), 19, 'string length is wrong 2')
assert.equal(s.str(), 'hello world foo 123', 'str failed')
