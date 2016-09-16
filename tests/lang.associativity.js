include('assert.js')

a = 2*3 + 4
b = 4 + 3*2

assert.equal(a, 10, 'multiplication gave incorrect result 1')
assert.equal(b, 10, 'multiplication gave incorrect result 2')

c = 0
d = c++ == 0
e = c++ <= 1
f = c++ < 3
g = c++ >= 3
h = c++ > 3
i = c++ != 4

assert.isTrue(d, 'associativity for ++ and == is wrong')
assert.isTrue(e, 'associativity for ++ and <= is wrong')
assert.isTrue(f, 'associativity for ++ and < is wrong')
assert.isTrue(g, 'associativity for ++ and >= is wrong')
assert.isTrue(h, 'associativity for ++ and > is wrong')
assert.isTrue(i, 'associativity for ++ and != is wrong')

j = 10
k = j-- == 10
l = j-- <= 9
m = j-- < 9
n = j-- >= 7
o = j-- > 5
p = j-- != 4

assert.isTrue(k, 'associativity for -- and == is wrong')
assert.isTrue(l, 'associativity for -- and <= is wrong')
assert.isTrue(m, 'associativity for -- and < is wrong')
assert.isTrue(n, 'associativity for -- and >= is wrong')
assert.isTrue(o, 'associativity for -- and > is wrong')
assert.isTrue(p, 'associativity for -- and != is wrong')

q = [1]
q[0]++
assert.equal(q[0], 2, 'post-increment failed for array indexer')
q[0]--
assert.equal(q[0], 1, 'post-decrement failed for array indexer')

// TODO: Test associativity of more operators here.
