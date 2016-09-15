include('../lib/array.js')
include('../lib/console.js')

a = Array([])
a.push('hej')
a.push('bosse')
a.push('och')
a.push('anita')
a.insert('carl', 2)
println(a.removeAt(0))
println('pop')

while (!a.isEmpty()) {
    println(a.pop())
}
