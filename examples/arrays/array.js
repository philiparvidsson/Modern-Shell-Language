include('array.js')
include('stdio.js')

// This example uses the mutable Array class provided by the mshl standard library.

a = array()

a.push('a')
a.push('c')

a.insert('b', 1)

while (a.length > 0) {
    println(a.pop())
}
