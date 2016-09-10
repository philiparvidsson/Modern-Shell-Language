include('inc/testing.js')

a = 'string1'
b = 'string2'
c = a+b

assert.areEqual(a, "string1", 'strings should be equal 1')
assert.areEqual(b, "string2", 'strings should be equal 2')
assert.areEqual(c, 'string1string2', 'string concat failed 1')

// Trying some complex concats below.

d = "'"
e = "'"
f = d+e

assert.areEqual(f, "''", 'string concat failed 2')

// Trying out 'weird' characters.

g = "!#¤'%)/("
// FIXME: failing chars: &=

// We don'ät have a better way of testing this yet, but we should
// proably iterate through the string and check each char.
assert.areEqual(g, "!#¤'%)/(", 'string contents are wrong')
