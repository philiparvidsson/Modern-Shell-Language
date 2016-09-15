include('assert.js')

a = 2*(3 + 4)
b = (4 + 3)*2

Assert.equal(a, 14, 'addition gave incorrect result 1')
Assert.equal(b, 14, 'addition gave incorrect result 2')
