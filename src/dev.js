include('../lib/console.js')
include('../lib/file.js')

f = File('../tests/file.txt')
println(f.exists())
println(f.read())
