include('assert.js')

a = 2*3 + 4
b = 4 + 3*2

Assert.equal(a, 10, 'multiplication gave incorrect result 1')
Assert.equal(b, 10, 'multiplication gave incorrect result 2')

c = 0
d = c++ == 0
e = c++ <= 1
f = c++ < 3
g = c++ >= 3
h = c++ > 3
i = c++ != 4

Assert.isTrue(d, 'associativity for ++ and == is wrong')
Assert.isTrue(e, 'associativity for ++ and <= is wrong')
Assert.isTrue(f, 'associativity for ++ and < is wrong')
Assert.isTrue(g, 'associativity for ++ and >= is wrong')
Assert.isTrue(h, 'associativity for ++ and > is wrong')
Assert.isTrue(i, 'associativity for ++ and != is wrong')

j = 10
k = j-- == 10
l = j-- <= 9
m = j-- < 9
n = j-- >= 7
o = j-- > 5
p = j-- != 4

Assert.isTrue(k, 'associativity for -- and == is wrong')
Assert.isTrue(l, 'associativity for -- and <= is wrong')
Assert.isTrue(m, 'associativity for -- and < is wrong')
Assert.isTrue(n, 'associativity for -- and >= is wrong')
Assert.isTrue(o, 'associativity for -- and > is wrong')
Assert.isTrue(p, 'associativity for -- and != is wrong')

q = [1]
q[0]++
Assert.equal(q[0], 2, 'post-increment failed for array indexer')
q[0]--
Assert.equal(q[0], 1, 'post-decrement failed for array indexer')

// TODO: Test associativity of more operators here.
