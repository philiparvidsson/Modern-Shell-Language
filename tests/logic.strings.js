include('assert.js')

a = 'string1'
b = 'string2'
c = a+b

assert.equal(a, "string1"       , 'strings should be equal 1')
assert.equal(b, "string2"       , 'strings should be equal 2')
assert.equal(c, 'string1string2', 'string concat failed 1')

// Trying some complex concats below.

d = "'"
e = "'"
f = d+e

assert.equal(f, "''", 'string concat failed 2')

g = '"'
h = '"'
i = g+h

assert.equal(i, '""', 'string concat failed 3')

// Trying out 'weird' characters.

j = "!#¤'%)/("
// FIXME: failing chars: &=

// We don't have a better way of testing this yet, but we should
// proably iterate through the string and check each char.
assert.equal(j, "!#¤'%)/(", 'string contents are wrong')
