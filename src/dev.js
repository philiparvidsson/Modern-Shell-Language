include('array.js')
include('stdio.js')

// This example uses the mutable Array class provided by the mshl standard library.

io.println('a')
a = array.new()

io.println('a')
a.push('a')
io.println('a')
a.push('c')
io.println('a')

io.println('a')
a.insert('b', 1)
io.println('123')

while (a.length > 0) {
io.println('p')

    io.println(a.pop())
    io.println('q')

}
io.println('z')
